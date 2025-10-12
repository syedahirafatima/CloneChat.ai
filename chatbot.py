import os
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

# Flask + OpenAI setup
app = Flask(__name__)
CORS(app)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "enter_your_openai_key_here":
    raise ValueError("Please set your OpenAI API key in the .env file!")

client = OpenAI(api_key=api_key)

@app.route("/")
def index():
    return send_file("chatbot_ui.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        conversation = data.get("conversation", [])
        if not conversation:
            return jsonify({"error": "Empty conversation"}), 400

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"\n🚀 Chatbot server running on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)
