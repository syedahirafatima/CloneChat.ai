# CloneChat.ai - Personalized AI Chatbot

✔️ A modern AI chatbot built with **Flask** and **OpenAI**. <br>
✔️ Users can set the bot's name and personality traits and chat interactively in a browser. <br> 
✔️ It has multilingual support; it understands and replies in the same language and tone you use, whether it’s English, French, Spanish, or more.<br> 
⚠️ This project is intended for **testing and demonstration purposes only**. Do **not** reuse, redistribute, or deploy commercially.


# Preview of the Chatting Screen
<img width="828" height="632" alt="Screenshot 2025-10-13 023938" src="https://github.com/user-attachments/assets/d495f3c2-e976-47fe-b518-5e5f5d09757f" />



# Recordings
- Dark/Light Mode Toggle: 
![dark and light demo](https://github.com/user-attachments/assets/8b9c3bed-88a5-4288-a636-963bc15af642)


- Sample Chat Session: 
![sample chat](https://github.com/user-attachments/assets/aef99cab-5414-4d8e-b69d-450d1a735d28)



---
---

# 💡 Why I Built This
➤ CloneChat was born from my own search for connection. I wanted to turn that feeling into something meaningful, a platform where people can shape their ideal companion or friend, express themselves freely, and feel heard, even in silence.<br> 

➤ To explore how AI can reflect human traits and emotions through language.

➤ To show how technology and empathy can work together in meaningful ways.

➤ To understand how OpenAI’s models handle personalized context and memory.

➤ To create a tool that feels human-like and emotionally aware, not robotic.

➤ To practice Flask backend + HTML/CSS/JS frontend integration.

# File Architecture
CloneChat.ai/<br>
├── .gitignore<br>
├── README.md<br>
├── chatbot.py<br>
├── chatbot_ui.html<br>
└── requirements.txt<br>

> `.env` is **not included** in this repo. Users need to create their own `.env` file with their OpenAI API key.

---

# Setup Instructions (How To Run It In Your PC)

Follow these steps to run the chatbot on your machine:

## 1️⃣ Clone the repository
```bash
git clone https://github.com/syedahirafatima/CloneChat.ai
cd CloneChat.ai
```
## 2️⃣ Create your .env file
Create a new file called .env in the root of the project:
```bash
OPENAI_API_KEY=your_openai_api_key_here
PORT=5000
```
Replace "your_openai_api_key_here" with your actual OpenAI API key.

## 3️⃣ Install dependencies
It’s recommended to use a Python virtual environment:
```bash
python -m venv venv
# Activate virtual environment
# Linux / Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```


## 4️⃣ Run the chatbot
```bash
python chatbot.py
```
The server will start at http://localhost:5000.
Open this URL in your browser to access the chatbot UI.


## 5️⃣ Using the chatbot
● Enter a bot name (e.g., Mom).<br>

● Enter personality traits (e.g., sweet, caring, supportive).<br>

● Click Apply to initialize the bot.<br>

● Type messages and click Send or press Enter.<br>

● Toggle Light/Dark mode using the button in the sidebar.<br>

## 📌 Notes

● This project is for testing and demonstration only.

● You must provide your own OpenAI API key.

● Works on any platform that supports Python 3.10+.

## 📌 Dependencies

1. Flask

2. flask-cors

3. openai

4. python-dotenv

(All required packages are listed in requirements.txt)

## 📌 License:
Under MIT license




