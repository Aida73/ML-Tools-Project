// Afficher les messages du chat
function displayMessage(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.className = 'message';
  const contentDiv = document.createElement('div');
  contentDiv.className = 'content';
  const messageParagraph = document.createElement('p');
  messageParagraph.textContent = message;
  contentDiv.appendChild(messageParagraph);
  messageDiv.appendChild(contentDiv);

  if (sender === 'user') {
    messageDiv.classList.add('user-message');
  } else {
    messageDiv.classList.add('bot-message');
  }

  document.getElementById('chat-container').appendChild(messageDiv);
  document.getElementById('chat-container').scrollTop = document.getElementById('chat-container').scrollHeight;
}

// Envoyer un message au chatbot via l'API
function sendMessage() {
  const userMessage = document.getElementById('userMessage').value;
  displayMessage(userMessage, 'user');

function handleEnterKey(event) {
  if (event.key === 'Enter') {
    sendMessage();
  }
}

  // Envoyer une requête à l'API
  fetch('http://da73.pythonanywhere.com', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question: userMessage }),
  })
    .then((response) => response.json())
    .then((data) => {
      const botResponse = data; 
      displayMessage(botResponse, 'bot');
    })
    .catch((error) => {
      console.error('Une erreur est survenue:', error);
      const errorMessage = "Il semble y avoir un problème, veuillez réessayer plus tard. Si le problème persiste, veuillez contacter le service technique à l'adresse suivante: tech@ept.sn";
      displayMessage(errorMessage, 'bot');
    });

  document.getElementById('userMessage').value = '';
}

document.body.addEventListener('scroll', function (e) {
  e.preventDefault();
});
