#include <iostream>
#include <cmath>
using namespace std;

bool isNeonNumber(int number) {
    int square = number * number;
    int sum = 0;
    while (square > 0) {
        int digit = square % 10;
        sum += digit;
        square /= 10;
    }
    return sum == number;
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    if (isNeonNumber(number)) {
        cout << number << " is a neon number." << endl;
    } else {
        cout << number << " is not a neon number." << endl;
    }
    return 0;
}
