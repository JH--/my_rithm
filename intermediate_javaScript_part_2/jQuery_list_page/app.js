$(document).ready(function () {
	$("#movie").submit( event => {
		event.preventDefault();
		let title = ($("#movieTitle").val() ? $("#movieTitle").val() : false);
		if (!title){
			$("#movieRating").val("");
			return;
		}
		let rating = $("#movieRating").val();
		rating = (rating >= 1 && rating <= 10 ? rating : 10); 
		let $row = $("<tr>");
		$row
		  .append($("<td>", {
		  	class: "text-center align-middle",
		    text: title
		  }))
		  .append($("<td>", {
		  	class: "text-center align-middle",
		  	text: rating
		  }))
		  .append($("<td>", {
		  	class: "text-center"
		  }).append($("<button>", {
		  	type: "button",
		  	class: "btn btn-danger",
		  	id: "delete",
		  	text: "Delete"
		  })))
		$("tbody").append($row);
		$("#movieTitle").val("");
		$("#movieRating").val("");
	})
	$("#movieTable").on("click", "#delete", event => $(event.target).parent().parent().remove());
})

/*
<tr>
	<td class="text-center align-middle">Star Wars The Last Jedi</td>
	<td class="text-center align-middle">8</td>
	<td class="text-center"><button type="button" class="btn btn-danger" id="delete">Delete</button></td>
</tr>
*/
