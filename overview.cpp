#include <iostream>
int main()

{   // define an integer variable named x
    int x1 = 0; // this variable is uninitialized because we haven't given it a value
    
    // print the value of x to the screen
    std::cout << x1 << '\n'; // who knows what we'll get, because x is uninitialized
    
    // there are 92 reserved words in C++
    
    
    std::cout << "Enter an Integer: ";
    int num{ };
    std::cin >> num ;
    
    int doubleNum{ num * 2};
    std::cout << "Double of " << num << " is " << doubleNum << "\n";
    
//    returnType functionName()
    return 0;
    /*
     this
     is
     a
     multline comment
     */
}
void doPrint(){
    std::cout << "In doPrint()\n";
}
