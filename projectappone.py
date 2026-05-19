import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
df = pd.read_csv(
    "spam.csv",
    sep='\t',
    names=['label', 'message']
)
X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
st.title("SMS Spam & Phishing Detector")

st.write(f"Model Accuracy: {accuracy * 100:.2f}%")
message = st.text_area("Enter SMS Message")
if st.button("Detect Message"):

    result = model.predict([message])[0]

    phishing_keywords = [
        "bank",
        "verify",
        "otp",
        "click",
        "urgent",
        "login",
        "password",
        "account",
        "suspended",
        "winner",
        "prize",
        "lottery",
        "free",
        "claim",
        "cashback",
        "income",
        "update",
        "verification",
        "block",
        "identity",
        "won",
        "security",
        "alert",
        "terminated",
        "compromised"
    ]

    keyword_detected = any(
        word in message.lower()
        for word in phishing_keywords
    )
    if result == "spam" or keyword_detected:

        st.error("⚠ SPAM / PHISHING MESSAGE DETECTED")

        st.subheader("Detected Suspicious Keywords:")

        for word in phishing_keywords:
            if word in message.lower():
                st.write("-", word)

    else:
        st.success("✅ SAFE MESSAGE")\
        