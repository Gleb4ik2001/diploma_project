function registerUser() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const registrationData = {
        email: document.getElementById('registrationEmail').value,
        password: document.getElementById('registrationPassword').value,
        first_name: document.getElementById('registrationFirstName').value,
        last_name: document.getElementById('registrationLastName').value
    };

    fetch('http://localhost:8000/auth/api/jobseeker_register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(registrationData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('User registered successfully');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Failed to register user');
    });
}