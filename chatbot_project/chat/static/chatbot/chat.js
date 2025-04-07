function sendMessage() {
    const userMessage = document.getElementById('user_message').value;
    const messagesDiv = document.getElementById('messages');
    
    fetch('/chat/', {
        method: 'POST',
        body: JSON.stringify({ 'message': userMessage }),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        messagesDiv.innerHTML += `<div class="user-message">${data.user_message}</div>`;
        messagesDiv.innerHTML += `<div class="bot-response">${data.bot_response}</div>`;
    });
}

function clearChat() {
    document.getElementById('messages').innerHTML = '';
}
