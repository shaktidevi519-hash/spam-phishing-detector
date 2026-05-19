# SMS Spam & Phishing Detector

A Machine Learning based web application that detects SMS spam and phishing messages using Natural Language Processing (NLP) and keyword-based phishing analysis.

Built using Python, Scikit-learn, and Streamlit.

---

## Features

- Detects spam SMS messages
- Detects phishing-related keywords
- Machine Learning classification using Naive Bayes
- Real-time message analysis
- Interactive Streamlit web interface
- Displays suspicious keywords detected in messages

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TfidfVectorizer
- Multinomial Naive Bayes

---

## Machine Learning Workflow

```text
Dataset
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Naive Bayes Training
   ↓
Prediction
   ↓
Phishing Keyword Analysis
   ↓
Result Display
```

---

## Dataset Format

The dataset file used is:

```text
spam.csv
```

Dataset structure:

| Label | Message |
|------|------|
| ham | Hello how are you |
| spam | Win a free lottery now |

---

## Project Structure

```text
sms-spam-detector/
│
├── app.py
├── spam.csv
├── requirements.txt
├── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sms-spam-detector.git
```

Move into the project folder:

```bash
cd sms-spam-detector
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## How It Works

### 1. TF-IDF Vectorization

The SMS message text is converted into numerical vectors using TF-IDF.

### 2. Naive Bayes Classification

The trained Multinomial Naive Bayes model predicts whether the message is:

- Spam
- Ham (Safe)

### 3. Phishing Keyword Detection

The application also scans for suspicious phishing keywords such as:

- OTP
- Verify
- Bank
- Password
- Login
- Winner
- Lottery
- Claim

If suspicious content is found, the application flags the message.

---

## Example Detection

### Input

```text
Your bank account has been suspended. Verify OTP immediately.
```

### Output

```text
⚠ SPAM / PHISHING MESSAGE DETECTED
```

Detected keywords:

```text
bank
verify
otp
suspended
```

---

## Future Improvements

- URL phishing detection
- Deep Learning models
- Probability confidence score
- Dark mode UI
- SMS history logging
- Real-time API integration
- Mobile responsive dashboard

---

## Author

Shaktidevi Pillai

---

## License

This project is created for educational and learning purposes.
