#include <iostream>
#include <string>

int main() {
  std::string username;
  std::string password;

  std::cout << "Enter username: ";
  std::cin >> username;

  std::cout << "Enter password: ";
  std::cin >> password;

  if (username == "admin" && password == "password") {
    std::cout << "Access granted" << std::endl;
  } else {
    std::cout << "Access denied" << std::endl;
  }

  return 0;
}
