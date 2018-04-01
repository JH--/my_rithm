//When the DOM is ready, console.log the message "Let's get ready to party with jQuery!"
$(document).ready(function () {
	console.log("Let's get ready to party with jQuery!");

	/*Give all images inside of an article tag the class of image-center 
	(this class is defined inside of the style tag in the head). */
	$("article img").addClass((i) => "image-center");

	//Remove the last paragraph in the article.
	$("article p:last-child").remove();

	//Set the font size of h1 with an id of title to be a random pixel size from 0 to 100.
	$("#title").css("font-size", `${Math.random() * (100 - 0) + 0}px`);

	//Add an item to the list; it can say whatever you want.
	const $newItem = $("<li>");
	$newItem.text("I'm a new item on the list added with jQuery");
	$("ol").append($newItem);

	/*Scratch that; the list is silly. Empty the aside and put a paragraph in it 
	apologizing for the list's existence.*/
	$("aside").empty();
	$newParagraph = $("<p>");
	$newParagraph.text("I'm sorry for showing you a list. I apologize that such a pointless thing ever existed.");
	$("aside").append($newParagraph);

	/*When you change the numbers in the three inputs on the bottom, the background color
    of the body should change to match whatever the three values in the inputs are.*/
    $("input").change(function () {
    	let red = $("input").eq(0).val();
    	let green = $("input").eq(1).val();
    	let blue = $("input").eq(2).val();
    	$("body").css("background-color", `rgb(${red}, ${green}, ${blue})`);
    })

	//Add an event listener so that when you click on the image, it is removed from the DOM.
	$("img").on("click", e => $(e.target).remove());
})

