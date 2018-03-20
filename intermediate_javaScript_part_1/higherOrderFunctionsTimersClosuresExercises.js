/* countdown accepts a number as a parameter and every 1000ms decrements the value
and console logs it. Once the value is 0 it console logs "DONE!" and stops. */


var countdown = function(i){
    setTimeout(function(){
        clearTimeout(timer);
        console.log("DONE!");
    }, i * 1000);
    var timer = setInterval(function() {
        --i;
        console.log(i);
    }, 1000)
}

countdown(11);

/* Random game selects a random number between 0 and 1 every 1000ms and each time
a random number is picked it adds 1 to a counter. If the number is great then 0.75
it stops the timer and returns the number of tries it took to find a number greater
then 0.75. */

function randomGame () {
    counter = 0;
    let timer = setInterval(function() {
        ++counter;
        let pick = Math.random();
        if (pick > 0.75) {
            clearTimeout(timer);
            console.log(counter);
        }
    }, 1000);
}

randomGame();

//isEven takes a number as a paramter and returns true if it's even flase it's odd

function isEven(i) {
    return i % 2 === 0;
}


//isOdd takes a number as a paramter and returns true if it's odd flase it's even

function isOdd(i) {
    return i % 2 !== 0;
}

/* isPrime takes a number as a parameter and returns true if it's a prime number
false if it's not. */


function isPrime(num){
    if (num <= 1) {
        return false;
    }
    for (i of [...Array(num).keys()].slice(2,num)) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}


/*numberFact takes as input a number and a callback and returns the result of
the callback with the number passed to it. */


function numberFact(i, fn){
    return fn(i);
}

/* find takes as input an array and a callback. It returns the first 
value that staisfies the condition of the callback. */


function find (arr, fn){
    for (i of arr) {
        if (fn(i)) {
            return i;
        }
    }
}

/* specialMultiply accepts 2 parameters. If the function is passed both parameters
it returns the product of the two. If specialMultiply is passed one parameter it
returns a function which can later be passed another parameter and return the product.*/

function specialMultiply (a, b) {
    if (arguments.length === 2) {
        return a * b;
    } else {
        return function (i) {
            return a * i;
        }
    }
}




/* findIndex takes as input an array and a callback. It returns the index of the
first value that staisfies the condition of the callback. */


function find (arr, fn){
    for (i in arr) {
        if (fn(arr[i])) {
            return i;
        }
    }
}






