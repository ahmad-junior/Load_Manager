// Allert Box
const allertBox = document.getElementById('alert-box');

// Close Button
const closeBtn = document.getElementById('closeBtn');


// Events
closeBtn.addEventListener('click', () => {
    allertBox.style.display = "none";
});