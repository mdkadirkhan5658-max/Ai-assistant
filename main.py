from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = "YOUR_API_KEY"

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": user_msg}]}]
    }
    response = requests.post(url, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
    
