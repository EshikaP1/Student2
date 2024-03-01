---
layout: default
title: Student Blog
---


---
layout: default
title: Student Blog
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
</head>
<body>
    <h2>Login</h2>
    <form id="loginForm">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>    
        <br> 
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="Login" onclick="authenticateUser()">
    </form>
    <script>
        function authenticateUser() {
            // Get username and password from the form
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;
            // Fetch user information based on the username (uid)
            fetch('/api/user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    uid: username,
                    password: password
                }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                // Handle the authentication response
                console.log('Authentication Response:', data);
                // Check if authentication is successful
                if (data.message === 'Authentication for ' + username + ' successful') {
                    // Authentication successful, perform further actions
                    console.log('Authentication successful');
                    // You can redirect the user to a secured area or perform other actions here
                } else {
                    // Authentication failed, display an error message
                    console.error('Authentication failed:', data.message);
                    // You can display an error message to the user or take other actions
                }
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle errors
            });
            // Prevent the form from submitting in the traditional way
            return false;
        }
    </script>
</body>
</html>


