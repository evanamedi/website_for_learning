// Get references to the dropdown menu and the dropdown button
var dropdownMenu = document.getElementById("dropdownMenu");
var dropdownButton = document.getElementById("dropdownButton");

// Show the dropdown menu when the dropdown button is clicked
dropdownButton.addEventListener("click", function (event) {
	event.stopPropagation();
	dropdownMenu.classList.toggle("hidden");
});

// Hide the dropdown menu when the user clicks outside of it
window.addEventListener("click", function (event) {
	dropdownMenu.classList.add("hidden");
});
