# 📧 Serverless Email API (Python)

This project is a simple **Serverless Framework Email API** built using **Python**.  
It runs locally using `serverless-offline` and allows sending emails by making a REST API request.

---

📂 Clone the Repository
# Clone the repo
git clone https://github.com/email-api/banao-task2.git

# Move into the project folder
cd email-api

## 🚀 Features
- Built with **Python** and the **Serverless Framework**
- Run locally with `serverless-offline`
- Exposes a REST API endpoint:  
  - `POST /send-email` → Sends an email to the specified recipient
- Uses SMTP credentials defined directly in `serverless.yml` (no `.env` file required)

---

## 📂 Project Structure
email-api/
│── handler.py # Lambda handler with email sending logic
│── serverless.yml # Serverless configuration (functions + SMTP credentials)
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── .gitignore # Ignore unnecessary files

yaml

---

## ⚙️ Setup & Installation

### 1️⃣ Install Serverless Framework
1. Install Serverless Framework
npm install -g serverless

2. Initialize NPM (for Serverless plugins)
npm init -y

3. Install required Serverless plugins
npm install --save serverless-offline serverless-python-requirements

4. Install Python dependencies
pip install -r requirements.txt

5. Start serverless-offline
serverless offline

📤 Usage
Endpoint:

POST http://localhost:3000/dev/send-email
Sample Request (JSON):

{
  "receiver_email": "example@gmail.com",
  "subject": "Test Email",
  "body_text": "Hello! This is a test email from Serverless Python API."
}
Sample Response (Success):

{
  "status": "success",
  "message": "Email sent successfully"
}
🛑 Error Handling
If an error occurs (e.g., invalid email, SMTP issue), the API will return:


{
  "status": "error",
  "message": "Error details here"
}