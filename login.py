# Define the username and password
username = "admin"
password = "password"

# Prompt the user to enter their username and password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

# Check if the entered username and password match the predefined credentials
if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Login failed. Incorrect username or password.")
