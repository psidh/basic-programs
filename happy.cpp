#include <iostream>
#include <unordered_set>
using namespace std;

int sumOfSquaredDigits(int number) {
    int sum = 0;
    while (number > 0) {
        int digit = number % 10;
        sum += digit * digit;
        number /= 10;
    }
    return sum;
}

bool isHappyNumber(int number) {
    unordered_set<int> seen;
    while (number != 1) {
        number = sumOfSquaredDigits(number);
        if (seen.count(number) > 0) {
            return false;
        }
        seen.insert(number);
    }
    return true;
}

int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;
    if (isHappyNumber(number)) {
        cout << number << " is a happy number." << endl;
    } else {
        cout << number << " is not a happy number." << endl;
    }
    return 0;
}
