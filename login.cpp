#include <iostream>
#include <string>

using namespace std;

int main() {

  string user = "admin";
  string pass = "password";


  string input_username;
  cout << "Enter your username: ";
  cin >> input_username;
  string input_password;
  cout << "Enter your password: ";
  cin >> input_password;

  // Check if the entered username and password match the predefined credentials
  if (input_username == user && input_password == pass) {
    cout << "Login successful!" << endl;
  } else {
    cout << "Login failed. Incorrect username or password." << endl;
  }
  
  return 0;
}
