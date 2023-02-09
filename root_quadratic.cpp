#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b, c;
    cout << "Enter the coefficient of x^2: ";
    cin >> a;
    cout << "Enter the coefficient of x: ";
    cin >> b;
    cout << "Enter the constant: ";
    cin >> c;
    double discriminant = b*b - 4*a*c;
    if (discriminant < 0) {
        cout << "The equation has no real roots." << endl;
    } else if (discriminant == 0) {
        double root = -b / (2 * a);
        cout << "The equation has one real root: " << root << endl;
    } else {
        double root1 = (-b + sqrt(discriminant)) / (2 * a);
        double root2 = (-b - sqrt(discriminant)) / (2 * a);
        cout << "The equation has two real roots: " << root1 << " and " << root2 << endl;
    }
    return 0;
}
