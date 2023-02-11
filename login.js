// Define the username and password
const username = "admin";
const password = "password";

// Prompt the user to enter their username and password
const inputUsername = prompt("Enter your username: ");
const inputPassword = prompt("Enter your password: ");

// Check if the entered username and password match the predefined credentials
if (inputUsername === username && inputPassword === password) {
  console.log("Login successful!");
} else {
  console.log("Login failed. Incorrect username or password.");
}
