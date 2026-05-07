document.getElementById('sendBtn').addEventListener('click', async () => {
    const question = document.getElementById('userInput').value;
    const output = document.getElementById('output');
    output.innerText = "Processing...";

    const res = await fetch('http://127.0.0.1:8000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    });
    const data = await res.json();
    output.innerText = data.answer;
});
