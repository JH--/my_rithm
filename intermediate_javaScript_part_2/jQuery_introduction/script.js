/*
Write the jQuery selectors/code to do the following

Write the necessary to code wait for the DOM to load in jQuery.
Select the footer element.
Select the div with an id of "container".
Select all of the lis inside of the ul with a class of nav.
Select the third li inside of the div with a class of list-container.
Select only the last li in each of the uls.
*/

$(function(){
	let $footer = $("footer");
	let $container = $("#container");
	let $nav = $(".nav .nav-item");   //$(".nav li")
	let $third_li = $(".nav-item").eq(2);  //$(".list-container li:nth-child(3)")
	let $nav_last = $(".nav-item").last();  //$("ul li:last-child") gets both last last li's
	let $third = $(".list-container li:nth-child(3)");
})

