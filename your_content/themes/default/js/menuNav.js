export function showOverlay(comicWorld) {
    const overlayDiv = comicWorld + "Overlay";
    const centeredDiv = document.getElementById(overlayDiv); // Get the centeredDiv by ID
    overlay.style.visibility = 'visible';
    centeredDiv.style.visibility = 'visible';
}
export function hideOverlay(comicWorld) {
    const overlayDiv = comicWorld + "Overlay";
    const centeredDiv = document.getElementById(overlayDiv); // Get the centeredDiv by ID
    overlay.style.visibility = 'hidden';
    centeredDiv.style.visibility = 'hidden';
}

export function revealMenu() {
	var element = document.getElementById("links-menu");
	element.classList.toggle("menuHide");
	var menuBar = document.getElementById("mobileMenu");
	menuBar.classList.toggle("menuToggled");
	var oneCycle = document.getElementsByClassName("ranOnce").length;
	var text = menuBar.innerHTML;
	if (text == "Show Menu" || oneCycle == 0) {
		menuBar.innerHTML = "Hide Menu";
	} else {
		menuBar.innerHTML = "Show Menu";
	}
	
	if (oneCycle == 0) {
	menuBar.classList.toggle("ranOnce");
	}
}