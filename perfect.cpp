#include <iostream>
#include <cmath>
using namespace std;

bool isPerfectNumber(int number) {
    int sum = 1;
    for (int i = 2; i <= sqrt(number); i++) {
        if (number % i == 0) {
            sum += i + number / i;
        }
    }
    return sum == number;
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    if (isPerfectNumber(number)) {
        cout << number << " is a perfect number." << endl;
    } else {
        cout << number << " is not a perfect number." << endl;
    }
    return 0;
}
