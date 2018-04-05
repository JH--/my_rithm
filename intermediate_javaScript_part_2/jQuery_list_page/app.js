$(document).ready(function () {
	
	const $tbody = $("tbody");

	$("#movie").submit( event => {
		event.preventDefault();
		let title = ($("#movieTitle").val() ? $("#movieTitle").val() : false);
		if (!title){
			$("#movieRating").val("");
			return;
		}
		let rating = $("#movieRating").val();
		rating = (rating >= 1 && rating <= 10 ? rating : 10); 
		$tbody.append(buildRow(title, rating));
		$("#movieTitle").val("");
		$("#movieRating").val("");
	})

	$tbody.on("click", "#delete", event => $(event.target).parent().parent().remove());

	$("thead").on("click", "#titleSort", event => {
		const rows = extractInfo(); 
		if(rows[0].title.toLowerCase() > rows[rows.length-1].title.toLowerCase()){
			rows.sort((a, b) => {
				if(a.title.toLowerCase() > b.title.toLowerCase()){return 1;}
				if(a.title.toLowerCase() < b.title.toLowerCase()){return -1;}
				return 0;
			})
		} else {
			rows.sort((a, b) => {
				if(a.title.toLowerCase() < b.title.toLowerCase()){return 1;}
				if(a.title.toLowerCase() > b.title.toLowerCase()){return -1;}
				return 0;
			})
		}
		$tbody.empty();
		rows.forEach(row => $tbody.append(buildRow(row.title, row.rating)));		
	});

	$("thead").on("click", "#ratingSort", event => {
		const rows = extractInfo();
		if(rows[0].rating > rows[rows.length-1].rating){
			rows.sort((a, b) => {
				if(a.rating > b.rating){return 1;}
				if(a.rating < b.rating){return -1;}
				return 0;
			})
		} else {
			rows.sort((a, b) => {
				if(a.rating < b.rating){return 1;}
				if(a.rating > b.rating){return -1;}
				return 0;
			})
		}
		$tbody.empty();
		rows.forEach(row => $tbody.append(buildRow(row.title, row.rating)));		
	});
})

function buildRow (title, rating){
	let $row = $("<tr>");
	return $row
	  .append($("<td>", {
	  	class: "text-center align-middle title",
	    text: title
	  }))
	  .append($("<td>", {
	  	class: "text-center align-middle rating",
	  	text: rating
	  }))
	  .append($("<td>", {
	  	class: "text-center"
	  }).append($("<button>", {
	  	type: "button",
	  	class: "btn btn-danger",
	  	id: "delete",
	  	text: "Delete"
	  })));
}

function extractInfo(){
  const titles = $(".title").map((i, row) => $(row).text()).get();
	const ratings = $(".rating").map((i, row) => $(row).text()).get();
	return titles.map((title, i) => ({"title": title, "rating": Number(ratings[i])}));
}
