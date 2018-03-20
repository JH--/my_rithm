What does the throw keyword do?

It throws an error object.

What does the finally keyword do?

It executes a bloc of code after a try except block sequence
regardless of which block of code was executed.

What is the difference between a TypeError and ReferenceError?

A ReferenceError is thrown when you refer to something that is 
undefined. A TypeError occurs when you try to use a method that
doesn't exist. ie Object.foo() where the foo property is undefined
and therefore cannot be a function that is executed.

How do you create a snippet in the Chrome dev tools?

You open chrome dev tools and click on the sources tab. Then in the 
left window you click on Snippets. Then you right click in the 
snippets space and select new.

What is an exception?

An exception is a thrown error object that is caught.

How do we catch errors in JavaScript? Give an example with code.

try {
	functionThatMightNotWork();
} catch(e) {
	console.log("The function didn't work. The error is ", e);
} 

or

try {
	if(function() === "something I don't like") {
		throw "I don't like that!";
	}
	console.log("Good answer!");
} catch(e) {
	console.log(e);
}

_______________________________________________________________________________

Explain what type of error will be thrown, why the error is occuring, and how to fix it:

1.
person;

A ReferenceError is thrown since person is undefined. You can fix this by defining person;

2.
var data = {};
data.displayInfo();

A TypeError is thrown since data.displayInfo === undefined and when you try to call undefined
as a function a TypeError is thrown. Fix it by defining the data.displayInfo function.

3.
var data = {};
data.displayInfo.foo = "bar";

A TypeError is thrown since data.displayInfo === undefined and when you call the foo method
a TypeError is thrown. Fix it by defining data.displayInfo.

4.
function data(){
	var thing = "foo";
}
data();
thing;

A ReferenceError is thrown since the thing variable only exists in the scope of the data 
function. Fix it by defining thing outside of the data function in the global scope.

________________________________________________________________________________

Fix the broken code and explain what was wrong:

1.
for(var i=0; i > 5; i++){
	console.log(i);
}

The i variable is initalized to 0 and therefore the greater then 5 condition is never valid.
The loop is never executed and nothing is logged.  One way to fix it is

for(var i=0; i < 5; i++){
	console.log(i);
}

2.
function addIfEven(num){
	if(num % 2 = 0){
		return num + 5;
	}
	return num;
}

num % 2 = 0 is an assignment not an equality test. Fix it like this

function addIfEven(num){
	if(num % 2 === 0){
		return num + 5;
	}
	return num;
}

3.
function loopToFive(){
	for(var i=0, i < 5, i++){
		console.log(i);
	}
}

Syntax error. The , is supposed to be ; in the for loop. Fix it like this

function loopToFive(){
	for(var i=0; i < 5; i++){
		console.log(i);
	}
}