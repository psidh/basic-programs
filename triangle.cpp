#include <iostream>
using namespace std;

int main() {
    int angle1, angle2;
    cout << "Enter the first angle of the triangle: ";
    cin >> angle1;
    cout << "Enter the second angle of the triangle: ";
    cin >> angle2;
    int angle3 = 180 - (angle1 + angle2);
    cout << "The third angle of the triangle is: " << angle3 << endl;
    return 0;
}
