import os
from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Global variables for our model
model = None
phishing_keywords = [
    "bank", "verify", "otp", "click", "urgent", "login", 
    "password", "account", "suspended", "winner", "prize", 
    "lottery", "free", "claim", "cashback", "income", "update", 
    "verification", "block", "identity", "won", "security", 
    "alert", "terminated", "compromised"
]

def init_model():
    """Trains the model once when the web server boots up."""
    global model
    file_path = "spam.csv"
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} missing!")
        return
        
    df = pd.read_csv(file_path, sep='\t', names=['label', 'message'])
    X = df['message']
    y = df['label']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', MultinomialNB())
    ])
    model.fit(X_train, y_train)
    print("🤖 Machine Learning Model trained and ready!")

# Train model immediately on script startup
init_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    result_text = None
    status_class = None
    detected_words = []
    user_message = ""

    if request.method == 'POST':
        user_message = request.form.get('message', '')
        
        if user_message.strip() and model is not None:
            # 1. ML Prediction
            ml_prediction = model.predict([user_message])[0]
            
            # 2. Heuristic Keyword Check
            clean_msg = user_message.lower()
            detected_words = [word for word in phishing_keywords if word in clean_msg]
            
            # 3. Decision Logic
            if ml_prediction.lower() == 'spam' or len(detected_words) > 0:
                result_text = "⚠️ SPAM / PHISHING DETECTED"
                status_class = "danger"
            else:
                result_text = "✅ THIS MESSAGE IS SAFE"
                status_class = "success"

    return render_template('index.html', 
                           result=result_text, 
                           status=status_class, 
                           keywords=detected_words,
                           previous_text=user_message)

if __name__ == '__main__':
    # Runs the local web server
    app.run(debug=True, port=5000)
