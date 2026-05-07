const API_KEY = 'AIzaSyCDLOzUflasL2zGzqH3xTS5ybcfpmLpWrc'; 
const API_URL = `https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=${API_KEY}`;

const SYSTEM_PROMPT = "তুমি একজন সিনিয়র ফুল-স্ট্যাক ডেভেলপার। মানুষের মতো নিখুঁত কোড লিখবে এবং বাংলায় কথা বলবে।";

async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const text = input.value.trim();
    if (!text) return;

    // ইউজার মেসেজ দেখানো
    chatBox.innerHTML += `<div class="message user">${text}</div>`;
    input.value = '';

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
                contents: [{ role: "user", parts: [{ text: text }] }]
            })
        });

        const data = await response.json();
        const aiResponse = data.candidates[0].content.parts[0].text;

        // এআই মেসেজ দেখানো
        chatBox.innerHTML += `<div class="message ai">${aiResponse.replace(/\n/g, '<br>')}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        chatBox.innerHTML += `<div class="message ai">ত্রুটি: এপিআই কানেক্ট হতে পারছে না।</div>`;
    }
}

document.getElementById('send-btn').addEventListener('click', sendMessage);
