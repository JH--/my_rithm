// 1. Select the section with an id of container without using querySelector

var container = document.getElementById("container");

//2. Select the section with and id of container using querySelector

var css_container = document.querySelector("#container");

//3. Select all of the list items with a class of "second"

var secondClass = document.getElementsByClassName("second");

//4. Select a list item with a class of third, but only the list item inside of the ol tag

var third_ol = document.querySelector("ol .third");

//5. Give the section with an id of container the text "Hello!"

container.innerText = "Hello!";

//6. Add the class main to the div with a class of footer

var footer = document.querySelector(".footer");
footer.classList.add("main");

//7. Remove the class main on the div with a class of footer

footer.classList.remove("main");

//8. Create a new li element

var newLi = document.createElement("li");

//9. Give the li the text "four"

newLi.innerText = "four";

//10. Append the li to the ul element

var ul = document.querySelector("ul");
ul.appendChild(newLi);

//11. Loop over all of the li's inside the ol tag and give them a background color of "green"

var olLi = document.querySelectorAll("ol li");
olLi.forEach(li => li.style.backgroundColor = "green");

/*
for(var i = 0; i < olLi.length; i++){
	olLi[i].style.backgroundColor = "green";
}
*/

//12. Remove the div with a class of footer

var body = document.getElementByTagName("body");
body.removeChild(footer);

/* 
var footer = document.querySelector(".footer");
footer.remove();
*/