// Allert Box
const allertBoxs = document.querySelectorAll('.alert-box');

// Close Button
const closeBtns = document.querySelectorAll('.closeBtn');


// Close Button
Array.from(closeBtns).forEach((closeBtn) => {
    closeBtn.addEventListener('click', () => {
        closeBtn.parentElement.style.display = "none";
    });
});