//Convert the following es5 code blocks into es2015 code:
/*
var person = {
    fullName: "Harry Potter",
    sayHi: function(){
        setTimeout(function(){
            console.log("Your name is " + this.fullName)
        }.bind(this),1000)
    }
}
*/
const person = {
    fullName: 'Harry Potter',
    sayHi: function (){
        setTimeout(() => console.log(`Your name is ${this.fullName}`), 1000)
    }
};

/*
var name = "Josie"
console.log("When " + name + " comes home, so good")
*/
const name = "Josie";
console.log(`When ${name} comes home, so good`);

/*
var DO_NOT_CHANGE = 42;
DO_NOT_CHANGE = 50; // stop me from doing this!
*/
const DO_NOT_CHANGE = 42;
DO_NOT_CHANGE = 50; //throws an error

/*
var arr = [1,2]
var temp = arr[0]
arr[0] = arr[1]
arr[1] = temp
*/
let arr = [1,2];
[arr[1], arr[0]] = [arr[0], arr[1]];

/*
function double(arr){
    return arr.map(function(val){
        return val*2
    });
}
*/
function double(arr){return arr.map(i => i*2)};

/*
var obj = {
    numbers: {
        a: 1,
        b: 2
    } 
}

var a = obj.numbers.a;
var b = obj.numbers.b;
*/
let obj = {
    numbers: {
        a: 1,
        b: 2
    }
};

let {a,b} = obj.numbers;

/*
function add(a,b){
    if(a === 0) a = 0
    else {
        a = a || 10    
    }
    if(b === 0) b = 0
    else {
        b = b || 10    
    }
    return a+b
}
*/
function add(a=10, b=10){return a + b};