/*
function buildRow(item){
	//item === ["item text", checked value(true or false)]
	const [text, checked] = item;
	const newRow = document.createElement("section");
	newRow.classList.add("row");
	const inputDiv = document.createElement("div");
	const input = document.createElement("input");
	input.type = "checkbox";
	if(checked){
		input.checked = true;
	}
	inputDiv.appendChild(input);
	newRow.appendChild(inputDiv);
	const itemDiv = document.createElement("div");
	itemDiv.classList.add("item");
	itemDiv.innerText = text;
	if(checked){
		itemDiv.style.textDecoration = "line-through";
	}
    newRow.appendChild(itemDiv);
	const delDiv = document.createElement("div");
	delDiv.classList.add("del");
	const del = document.createElement("button");
	del.classList.add("delete");
	const delIcon = document.createElement("i");
	delIcon.classList.add("material-icons");
	delIcon.innerText = "delete";
	del.appendChild(delIcon);
	delDiv.appendChild(del);
	newRow.appendChild(delDiv);
	return newRow;
}
*/

function buildCheckBox(checked){
	const inputDiv = document.createElement("div");
	const input = document.createElement("input");
	input.type = "checkbox";
	if(checked){
		input.checked = true;
	}
	inputDiv.appendChild(input);
	return inputDiv;
}

function buildItem(text, checked){
	const itemDiv = document.createElement("div");
	itemDiv.classList.add("item");
	itemDiv.innerText = text;
	if(checked){
		itemDiv.style.textDecoration = "line-through";
	}
	return itemDiv;	
}

function buildDelete(){
	const delDiv = document.createElement("div");
	delDiv.classList.add("del");
	const del = document.createElement("button");
	del.classList.add("delete");
	const delIcon = document.createElement("i");
	delIcon.classList.add("material-icons");
	delIcon.innerText = "delete";
	del.appendChild(delIcon);
	delDiv.appendChild(del);
	return delDiv;	
}

function buildRow(item){
	//item === ["item text", checked value(true or false)]
	const [text, checked] = item;
	const newRow = document.createElement("section");
	newRow.classList.add("row");
	newRow.appendChild(buildCheckBox(checked));
	newRow.appendChild(buildItem(text, checked));
	newRow.appendChild(buildDelete());
	return newRow;
}

function updateLocalStorage() {
	localStorage.clear();
	const items = [];
	const list = document.getElementById("list");
	for(child of list.children){
		const checked = child.children[0].children[0].checked;
		const item = child.children[1].innerText;
		items.push([item, checked]);
	}
	localStorage.setItem("items", JSON.stringify(items));
}

function refresh(list){
	const items = JSON.parse(localStorage.getItem("items"));
	if(items){
		items.forEach(item => list.appendChild(buildRow(item)));
	}
}

document.addEventListener("DOMContentLoaded", function () {
	const list = document.getElementById("list");
	refresh(list);
	list.addEventListener("click", e => {
		if(e.target.parentElement.getAttribute("class") === "delete"){
			e.target.parentElement.parentElement.parentElement.remove();
			updateLocalStorage();
		}
	});
	list.addEventListener("change", e => {
		if(e.target.checked){
			e.target.parentElement.parentElement.children[1].style.textDecoration = "line-through";
		} else {
			e.target.parentElement.parentElement.children[1].style.textDecoration = "none";
		}
		updateLocalStorage();
	})
	const addButton = document.getElementById("add");
	addButton.addEventListener("click", e => {
		if(document.querySelector("input").value){
			list.appendChild(buildRow([document.querySelector("input").value, false]));
			document.querySelector("input").value = "";
		};
		updateLocalStorage();
		e.preventDefault();	
	});
})








/*
function buildRow(item){
	//item === ["item text", checked value(true or false)]
	const [text, checked] = item;
	const newRow = document.createElement("section");
	newRow.classList.add("row");
	const inputDiv = document.createElement("div");
	const input = document.createElement("input");
	input.type = "checkbox";
	if(checked){
		input.checked = true;
	}
	inputDiv.appendChild(input);
	newRow.appendChild(inputDiv);
	const itemDiv = document.createElement("div");
	itemDiv.classList.add("item");
	itemDiv.innerText = text;
	if(checked){
		itemDiv.style.textDecoration = "line-through";
	}
    newRow.appendChild(itemDiv);
	const delDiv = document.createElement("div");
	delDiv.classList.add("delete");
	const del = document.createElement("button");
	del.classList.add("del");
	const delIcon = document.createElement("i");
	delIcon.classList.add("material-icons");
	delIcon.innerText = "delete";
	del.appendChild(delIcon);
	delDiv.appendChild(del);
	newRow.appendChild(delDiv);
	input.addEventListener("change", e => {
		if(input.checked){
			itemDiv.style.textDecoration = "line-through";
		} else {
			itemDiv.style.textDecoration = "none";
		}
		updateLocalStorage();
	})
	del.addEventListener("click", e => {
		e.target.parentElement.parentElement.parentElement.remove();
		updateLocalStorage();
	});
	return newRow;
}

function updateLocalStorage() {
	localStorage.clear();
	const items = [];
	const list = document.getElementById("list");
	for(child of list.children){
		const checked = child.children[0].children[0].checked;
		const item = child.children[1].innerText;
		items.push([item, checked]);
	}
	localStorage.setItem("items", JSON.stringify(items));
}

function  refresh(list){
	const items = JSON.parse(localStorage.getItem("items"));
	if(items){
		items.forEach(item => list.appendChild(buildRow(item)));
	}
}

document.addEventListener("DOMContentLoaded", function () {
	const list = document.getElementById("list");
	refresh(list);
	const addButton = document.getElementById("add");
	addButton.addEventListener("click", e => {
		if(document.querySelector("input").value){
			list.appendChild(buildRow([document.querySelector("input").value, false]));
			document.querySelector("input").value = "";
		};
		updateLocalStorage();
		e.preventDefault();	
	});
})
*/











/*
document.addEventListener("DOMContentLoaded", function () {
	const list = document.getElementById("list");
	const addButton = document.getElementById("add");
	addButton.addEventListener("click", e => {
		if(document.querySelector("input").value){
			const newRow = document.createElement("section");
			newRow.classList.add("row");
			const inputDiv = document.createElement("div");
			const input = document.createElement("input");
			input.type = "checkbox";
			inputDiv.appendChild(input);
			newRow.appendChild(inputDiv);
			const itemDiv = document.createElement("div");
			itemDiv.classList.add("item");
			itemDiv.innerText = document.querySelector("input").value;
			newRow.appendChild(itemDiv);
			const delDiv = document.createElement("div");
			delDiv.classList.add("delete");
			const del = document.createElement("button");
			del.classList.add("del");
			const delIcon = document.createElement("i");
			delIcon.classList.add("material-icons");
			delIcon.innerText = "delete";
			del.appendChild(delIcon);
			delDiv.appendChild(del);
			newRow.appendChild(delDiv);
			list.appendChild(newRow);
			input.addEventListener("change", e => {
				if(input.checked){
					itemDiv.style.textDecoration = "line-through";
				} else {
					itemDiv.style.textDecoration = "none";
				}
			})
			del.addEventListener("click", e => {
				e.target.parentElement.parentElement.parentElement.remove();
			});
			document.querySelector("input").value = "";
		};
		e.preventDefault();
	});
})
*/


/*
<section class="row">
			<div><input type="checkbox"></div>
			<div class="item">buy milk</div>
			<div class="del"><button class="delete"><i class="material-icons">delete</i></button></div>
		</section>

*/
