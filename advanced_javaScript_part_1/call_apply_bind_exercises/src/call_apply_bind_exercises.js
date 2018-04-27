/*Write a function called sumEvenArguments which takes all of the arguments 
passed to a function and returns the sum of the even ones. */

function sumEvenArguments() {
	return [].slice.call(arguments).
	       filter(i => i%2 === 0).
	       reduce((acc, next) => acc + next, 0);
};

//Write a function called arrayFrom which converts an array-like-object into an array.

function arrayFrom() {
	return [].slice.call(arguments);
};

/*Write a function called invokeMax which accepts a function and a maximum 
amount. invokeMax should return a function that when called increments a 
counter. If the counter is greater than the maximum amount, the inner 
function should return "Maxed Out!" */

function invokeMax(fn, maxAmt){
	let counter = 0;
	return function(){
		if(counter >= maxAmt){
			return "Maxed Out!";
		} else {
			counter += 1;
			return fn.apply(this, arguments);
		}
	}
};

/*Write a function called guessingGame which takes in one parameter amount.
The function should return another function that takes in a parameter called 
guess. In the outer function, you should create a variable called answer which
is the result of a random number between 0 and 10 as well as a variable 
called guesses which should be set to 0. In the inner function, if the guess
passed in is the same as the random number (defined in the outer function) - 
you should return the string "You got it!". If the guess is too high return 
"You're too high!" and if it is too low, return "You're too low!". You should
stop the user from guessing if the amount of guesses they have made is greater
than the initial amount passed to the outer function. You will have to make 
use of closure to solve this problem. */

function guessingGame(tries){
	let answer = Math.floor(Math.random() * 10);
	let guesses = 0;
	let finished = false;
	return function(guess){
		guesses += 1;
		if(!finished){
			if(guess != answer && guesses === tries){
				finished = true;
				return `No more guesses the answer was ${answer}.`;
			}
			if(guess === answer){
				finished = true;
				return "You got it!"
			}else if(guess > answer){
				return "You're too high!";
			}else if(guess < answer){
				return "You're too low!";
			} 
		};
		return "You're all done playing!";
	};
};
