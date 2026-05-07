import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# আপনার এপিআই কী এখানে বসান
API_KEY = "AIzaSyCDLOzUflasL2zGzqH3xTS5ybcfpmLpWrc"
genai.configure(api_key=API_KEY)

# এআই-এর জন্য নিখুঁত ভূমিকা (System Instruction)
SYSTEM_PROMPT = """তোমার নাম "কোড-মাস্টার এআই"। তুমি ক্লড (Claude) বা সিনিয়র ডেভেলপারদের মতো দক্ষ। 
১. মানুষের মতো সাবলীল বাংলায় কথা বলবে। 
২. কোড ব্লকের বাইরে লজিকগুলো সুন্দর করে বুঝিয়ে দিবে। 
৩. কোড হবে আধুনিক এবং ইন্ডাস্ট্রি স্ট্যান্ডার্ড। 
৪. ব্যবহারকারীকে একজন প্রো-ডেভেলপার পার্টনার হিসেবে গাইড করবে।"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    try:
        response = model.generate_content(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
