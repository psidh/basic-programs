#include <iostream>

using namespace std;

int main() {
    float maths, science, english, total, average, percentage;

    cout << "Enter marks in Maths: ";
    cin >> maths;

    cout << "Enter marks in Science: ";
    cin >> science;

    cout << "Enter marks in English: ";
    cin >> english;

    total = maths + science + english;
    average = total / 3.0;
    percentage = (total / 300.0) * 100;

    cout << "Total marks: " << total << endl;
    cout << "Average marks: " << average << endl;
    cout << "Percentage: " << percentage << endl;

    return 0;
}
