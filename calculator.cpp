#include <iostream>

using namespace std;

int main() {
  float num1, num2;
  char operation;
  float result;
  cout << "Enter the first number: ";
  cin >> num1;
  cout << "Enter the second number: ";
  cin >> num2;
  cout << "Enter an operation (+, -, *, /): ";
  cin >> operation;
  switch (operation) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      result = num1 / num2;
      break;
    default:
      cout << "Invalid operator" << endl;
      return 0;
  }
  cout << "Result: " << result << endl;
  return 0;
}
