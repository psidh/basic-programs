// this overview is being created by learning everything from https://w3schools.com/js


// output in js
// accessing html element in javascript we use the following

// <!DOCTYPE html>
<html>
<body>

<h1>My First Web Page</h1>
<p>My First Paragraph</p>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = 5 + 6;
</script>

</body>
</html>

//______________________________________________________________

//another methhod used for the samw purpose is 

//dcoument.write - used only for testing

// third method is window.alert():

// fourth method is alert();

// the general one that we use it console.log()

//__________________________________________________

// variable declaration in javascript L:

var name = "SIdharth";
var age  = 18;
var isStudent = false; // boolean operator
var favpouritecolour = null;

//constants 

const pi = 3.14

// operators in javascript are same as in all typical programming languages

//assigning a value o the variable is done by following

let text = "Hello"; text += " World";

//__________________________________________________


// conditional statetments
// if and else if , and else and switch
if (hour < 18) {
  greeting = "Good day";
}

/*

if (condition1) {
  //  block of code to be executed if condition1 is true
} else if (condition2) {
  //  block of code to be executed if the condition1 is false and condition2 is true
} else {
  //  block of code to be executed if the condition1 is false and condition2 is false
}


for (let i = 0; i < 10; i++) {
  if (i === 3) { break; }
  text += "The number is " + i + "<br>";
}

*/
//____________________________________________________________

// now lets discuss and concentrate on bitwise operators

// logical operators && , ||  and ??=


//javascript has 8 datatypes 


/* 

string
number
bigint
boolean
udefined
null
symbol
object

*/


/*

object datatypes in js

an object
an array
a date

*/

if (age > 18){
    console.log("You are eligible for voting.");

} else {
    console.log("YOua re onot eligible for voting.");

}


// funtions in javascript

function addNumbers(num1, num2){
    return num1+num2
} 

var result = addNumbers(10, 890);
console.log(result) //  outputs are 900




// Numbers:
let length = 16;
let weight = 7.5;

// Strings:
let color = "Yellow";
let lastName = "Johnson";

// Booleans
let x = true;
let y = false;

// Object:
const person = {firstName:"John", lastName:"Doe"};

// Array object:
const cars = ["Saab", "Volvo", "BMW"];

// Date object:
const date = new Date("2022-03-25");


// like other languages javascript has array 
const cars2 = ["Saab", "Volvo", "BMW"];

//OOPS support in JS
const person2 = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};

/* creating an object then requires objectName.propertyName
like person2.firstName

syntax for determining the datatype is typeof

we also have undefined and empty values and both are significantly different

Function to compute the product of p1 and p2  a fucntion with a parameter */

// notation of exponential

let es= 123e-8;




// functions in js

function myFunction(p1, p2) {
    return p1 * p2;
  }

const person3 = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    fullName : function() {
      return this.firstName + " " + this.lastName;
    }
};
// 'this' refers to the person3 object

// accessing objects is done through objectName.methodName()


// the below should not be done !!
x = new String();        // Declares x as a String object 
y = new Number();        // Declares y as a Number object
z = new Boolean();       // Declares z as a Boolean object



// discussing the html events

/* 

events like

-just finished loading 
-input field changed
-button *clicked


additionn of javascript code into html

<element event='some JavaScript'>

onclick attribute to <button>

<button onclick="document.getElementById('demo').innerHTML = Date()">The time is?</button>



common html events

"onchange" : hmtl element has been changed
"onclick" : 
"onmouseout": user moves the mouse over the html element
"onmouseout": user moves away fromt he html element

JavaScript Event Handlers
Event handlers can be used to handle and verify user input, user actions, and browser actions:

*/


// Strings in js
// let carName1 = "Volvo XC60";  // Double quotes
let text4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let length1 = text.length;



/* escape characte 
let text = "We are the so-called \"Vikings\" from the north.";
== operator is a boolena operator

*/



// THE BELOW ONE ARE VERY IMPORTANT REGARDING STRING SLICING

/*
THE METHODS IN  STRINGS

String length
String slice()
String substring()
String substr()
String replace()
String replaceAll()
String toUpperCase()
String toLowerCase()
String concat()
String trim()
String trimStart()
String trimEnd()
String padStart()
String padEnd()
String charAt()
String charCodeAt()
String split()


*/
 //lets use some of these in the upcoming programs

 // string length

 let test1 = "my name is p sidharth";
console.log(test1.length) ;
//threee extraciton in stirng , parts , are
/*
slice
substring
substr(start, length)

*/


//___________________________________________
//javascript string search


/* methods in string seaccrh in javascript

String indexOf()
String lastIndexOf()
String search()
String match()
String matchAll()
String includes()
String startsWith()
String endsWith()

*/

// JAVASCRIPT TEMPLATE LITERALS

//  BACK TICKS ``

// F STRING type of concept in JAVSCRIPT is  called INTERPOLATION`welcome to ${gitam} deemed to be university`


// XPRESSIOJN SUBSTITUTION  - `Total: ${(price * (1 + VAT)).toFixed(2)}`;


/* JavaScript Number Methods

toString()	            Returns a number as a string
toExponential()     	Returns a number written in exponential notation
toFixed()	            Returns a number written with a number of decimals
toPrecision()	        Returns a number written with a specified length
ValueOf()	            Returns a number as a number

*/


//_________________________________________________________________



// array in a javascript

var subjects = ["maths", "english", "cse", "chemistry"];

// accessing array elements 

subjects[0];

//changing array element

subjects[0] == "Opel";

// array as objects

const player_one = {firstName:"John", lastName:"Doe", age:46};

// looping the arrays

const fruits = ["Banana", "Orange", "Apple", "Mango"];
let fLen = fruits.length;

let text3 = "<ul>";
for (let i = 0; i < fLen; i++) {
  text += "<li>" + fruits[i] + "</li>";
}
text += "</ul>";

// the above is a general for loop , similar to C lang and Java
// adding elements in an array 
fruits.push("lemom");
fruits.pop()

/*
The Difference Between Arrays and Objects
In JavaScript, arrays use numbered indexes.  

In JavaScript, objects use named indexes

getting to know something is an array

Array.isArray(fruits);



*/



//______Array conversion to string__________________________


fruits.toString();

//popping an pushing

// sorting an array is very easy in javascript

fruits.sort();

// Find the Highest (or Lowest) Array Value

// math max , highest nunmber in an array
function myArrayMax(arr) {
    return Math.max.apply(null, arr);
  }

// array map
const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);

function myFunction(value, index, array) {
  return value * 2;
}

// array filter

const numbers = [45, 4, 9, 16, 25];
const over18 = numbers.filter(myFunction);

function myFunction(value, index, array) {
  return value > 18;
}

// date objects - new date()

// MAth.pi
/* Math.E        // returns Euler's number
Math.PI       // returns PI
Math.SQRT2    // returns the square root of 2
Math.SQRT1_2  // returns the square root of 1/2
Math.LN2      // returns the natural logarithm of 2
Math.LN10     // returns the natural logarithm of 10
Math.LOG2E    // returns base 2 logarithm of E
Math.LOG10E   // returns base 10 logarithm of E

math methods


Math.round(x)	Returns x rounded to its nearest integer
Math.ceil(x)	Returns x rounded up to its nearest integer
Math.floor(x)	Returns x rounded down to its nearest integer
Math.trunc(x)	Returns the integer part of x (new in ES6)


Math.pow(8,2);

Math.min() and Math.max()

Math.random();
 
Essential Map Methods
Method	Description
new Map()	Creates a new Map
set()	Sets the value for a key in a Map
get()	Gets the value for a key in a Map
delete()	Removes a Map element specified by the key
has()	Returns true if a key exists in a Map
forEach()	Calls a function for each key/value pair in a Map
entries()	Returns an iterator with the [key, value] pairs in a Map
Property	Description
size	Returns the number of elements in a Map

//__________________________________________________________


JavaScript Hoisting

x = 5; // Assign 5 to x

elem = document.getElementById("demo"); // Find an element 
elem.innerHTML = x;                     // Display x in the element

var x; // Declare x

__________________________________________________________-

JS Precedence is exactly like python arithmetic operations

_____________________________________________________________-

The try statement defines a code block to run (to try).

The catch statement defines a code block to handle any error.

The finally statement defines a code block to run regardless of the result.

The throw statement defines a custom error.


*/
//____________________________________________________________________
<p id="demo"></p>

<script>
try {
  adddlert("Welcome guest!");
}
catch(err) {
  document.getElementById("demo").innerHTML = err.message;
}
</script>
//____________________________________________________________________
