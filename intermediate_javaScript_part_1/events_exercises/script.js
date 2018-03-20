/*Add the necessary code to wait for the DOM to load to make sure that anything you manipulate in the DOM has loaded. 
You can do this either using window.onload or adding an event listener for DOMContentLoaded. */

document.addEventListener("DOMContentLoaded", function () {
    //Replace the text "Change me" with "Hello World!".
    document.getElementById("change_heading").innerText = "Hello World!";

    /*When a user hovers over one of the colored boxes change the text to 
    display the color that is being hovered over. */
    let section = document.querySelector("section");
    section.addEventListener("mouseover", event => document.querySelector(".selected").innerText = event.target.className || "None!");
    section.addEventListener("mouseleave", event => document.querySelector(".selected").innerText = "None!");

    //Create a new div element.
    let newDiv = document.createElement("div");

    //Give your new div a class of purple and style it so that it has a background color of purple.
    newDiv.classList.add("purple");
    newDiv.style.backgroundColor = "purple";

    //Append your new div to the page to the section tag.
    section.append(newDiv);

    /*Create a racing game with the two cars. When the race button is pressed, the two cars should 
    move across the screen until one of them is at the end of the screen. When one of the blocks 
    reaches the end - you should alert "winner!" */
    let button = document.querySelector("button");
    let car1 = document.querySelector(".car1");
    let car1Pos = 0;
    let car2 = document.querySelector(".car2");
    let car2Pos = 0;
    let goal = window.innerWidth;
    function getRandomInt(max){
    	return Math.floor(Math.random() * Math.floor(max));
    }
    function reset(){
    	[car1Pos, car2Pos] = [0, 0];
    	car1.style.transform = "translate(0px)";
    	car2.style.transform = "translate(0px)";
    	button.innerText = "Start the race!";
    }
    button.addEventListener("click", event => {
    	button.innerText = "Keep racing!";
    	car1.style.transform = `translate(${car1Pos += getRandomInt(300)}px)`;
    	car2.style.transform = `translate(${car2Pos += getRandomInt(300)}px)`;
    	if((car1Pos >= goal && car2Pos >= goal) && car1Pos > car2Pos){
    		setTimeout(() => {
    			alert("Car 1 is the winner!");
    		    reset();
    		}, 300);
    	} else if((car2Pos >= goal && car1Pos >= goal) && car2Pos > car1Pos){
    		setTimeout(() => {
    			alert("Car 2 is the winner!");
    		    reset();
    		}, 300);
    	} else if(car1Pos >= goal){
    		setTimeout(() => {
    			alert("Car 1 is the winner!");
    		    reset();
    		}, 300);
    	} else if(car2Pos >= goal){
    		setTimeout(() => {
    			alert("Car 2 is the winner!");
    		    reset();
    		}, 300);
    	}	
    })
})