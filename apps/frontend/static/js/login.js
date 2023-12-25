function loginUser() {
    const loginData = {
        email: document.getElementById('loginEmail').value,
        password: document.getElementById('loginPassword').value,
    };

    fetch('http://localhost:8000/auth/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  // Добавляем CSRF-токен в заголовки
        },
        credentials: 'same-origin',  // Убедитесь, что credentials установлены в 'same-origin'
        body: JSON.stringify(loginData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Authentication successful');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Authentication failed');
    });
}

// Функция для получения значения CSRF-токена из cookie
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
