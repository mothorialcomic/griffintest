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