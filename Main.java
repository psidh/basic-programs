public class Main {


    public int xy;

    static int add(int a1, int a2){
        return a1+a2;

    }
    public static void main(String[] args) {
        String name = "P SIdharth";

        System.out.println("My name is "+ name);
        System.out.println("Hi I am a complete beginner in JAVA.");

        float f1 = 35e3f;
        double d1 = 12E4d;
        System.out.println(f1);
        System.out.println(d1);

        //  character examples
        char myGrade = 'B';
        System.out.println(myGrade);

        // string examples below
        String var = "this is an variable";
        System.out.println(var);

        //type casting example
        double myDouble = 9.78d;
        int myInt = (int) myDouble; // Manual casting: double to int
        // the decimal places are removed, so it's not round off

        System.out.println(myDouble);   // Outputs 9.78
        System.out.println(myInt);

        // some string functions in java
        String txt = "Hello World";

        System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
        System.out.println(txt.toLowerCase());

        // few more
        String text = "Please locate where 'locate' occurs!";
        System.out.println(text.indexOf("locate")); // Outputs 7

        // concatenation of two set of strings
        String firstName = "John ";
        String lastName = "Doe";

        System.out.println(firstName.concat(lastName));
        System.out.println(lastName.concat(firstName));

        // special characters in java
        String text2 = "We are the so-called \"Vikings\" from the north.";
        System.out.println(text2); // to generate the double quotes inside the print statement

        String text3 = "It\'s alright.";
        System.out.println(text3);

        String text4 = "The character \\ is called backslash."; ///  tp print  a backslash in the print statement

        //Maths in java

        Math.max(4, 5);

        Math.min(1, 3);

        Math.sqrt(25);

        int random = (int)(Math.random()*2);
            // similar to python there are boolean operators in java
        //  there exists some conditional statements like if and else
        if (20>19){
            System.out.println("20 is greater than 19");
        } else{
            System.out.println("19 is greater than 20");}

        // there exists switch and cases like c in java
        int i = 0;
        do {
           System.out.println(i);
           i= i+1;

         } while(i<3);

        int k = 0;

        for( k = 0;k<6 ; k++) {
               System.out.println(i);
           }
        // break and continue statements are same in as in java asnin c\
        // array are just like lists in pytohn
        //loops in array
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (int n = 0; i < cars.length; i++) {
            System.out.println(cars[i]);
        }
        // multidimensional arrays

        int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
        for (int l = 0; l < myNumbers.length; ++l) {
            for(int j = 0; j < myNumbers[l].length; ++j) {
                System.out.println(myNumbers[l][j]);
            }
        }
        // multiple parameters

        int mynumber = add(6, 7);
        System.out.println(mynumber);
//__________________________________________________


        int result = sum(5, 10);
        System.out.println(result);
    }
        public static int sum(int start, int end) {
            if (end > start) {
                return end + sum(start, end - 1);
        } else {
                return end;
        }


//_________________________________________________


    }


}




