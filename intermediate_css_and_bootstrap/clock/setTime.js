function setTime(){
	const date = new Date;
	const seconds = date.getSeconds();
	const minutes = date.getMinutes();
	const hours = date.getHours();
	const secondHand = document.querySelector(".second");
	const minuteHand = document.querySelector(".minute");
	const hourHand = document.querySelector(".hour");
	secondHand.style.transform = `rotate(${seconds * 6}deg)`;
	minuteHand.style.transform = `rotate(${minutes * 6}deg)`;
	hourHand.style.transform = `rotate(${(hours * 30) + (minutes / 2)}deg)`;
}

document.addEventListener("DOMContentLoaded", () => setTime());