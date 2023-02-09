#include <iostream>
using namespace std;

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

int main() {
    int num;
    cout << "Enter the number of terms: ";
    cin >> num;
    cout << "The first " << num << " terms of the fibonacci series are: ";
    for (int i = 0; i < num; i++) {
        cout << fibonacci(i) << " ";
    }
    cout << endl;
    return 0;
}
