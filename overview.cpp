#include <iostream>

int main()

{
    std::cout << "Srinivas";
    
    // this line prints the expression as output
    int a = 9;         // no initializer (default initialization)
    int b = 5;     // initializer after equals sign (copy initialization)
    int c( 6 );    // initializer in parenthesis (direct initialization)
    std::cout << (a+ b+ c) ;
    
    // List initialization methods (C++11)
    int d { 7 };   // initializer in braces (direct list initialization)
    int e = { 8 }; // initializer in braces after equals sign (copy list initialization)
    int f {};      // initializer is empty braces (value initialization)
    std::cout << d+ e+ f ;
    
    //int x();  // forward declaration of function x
    // int x(0); // definition of variable x with initializer 0

    int width { 5 };    // direct list initialization of value 5 into variable width (preferred)
    int height = { 6 }; // copy list initialization of value 6 into variable height
    //int depth {};       // value initialization (see next section)
    
    std::cout << width + height;
    
    //  [[maybe_unused]] int x1 { 5 };

    // since x is [[maybe_unused]], no warning generated
    std::cout << 4 << "\n";
    std::cout << 6 << "\n";

    int my_number;

    std::cout << "Enter a number: " ;
    std::cin >> my_number;
    std::cout << "You entered the input: " << my_number << "\n";

    std::cout << "Enter two numbers separated by a space: ";

    int x{ }; // define variable x to hold user input (and zero-initialize it)
    int y{ }; // define variable y to hold user input (and zero-initialize it)
    std::cin >> x >> y; // get two numbers and store in variable x and y respectively

    std::cout << "The numbers are " << x << " and " << y << '\n';

    return 0;
    
    /*
     this
     is
     a
     multline comment
     */
}
