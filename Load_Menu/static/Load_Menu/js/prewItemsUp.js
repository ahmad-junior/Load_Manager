    // Buttons
const   updateBtnPI = document.getElementById('updateBtnPI'),
    btnCancelPI = document.getElementById('btnCancelPI'),
    btnOKPI = document.getElementById('btnOKPI');

// Contents
const popUpContent = document.getElementById('popUpContent');

// Box
const popupBox = document.getElementById('popupBox');

// Events
updateBtnPI.addEventListener('click', () =>{
popupBox.style.display = 'flex';
popUpContent.innerText = "Are you sure to Update this item?";
})

btnCancelPI.addEventListener('click', () =>{
popupBox.style.display = 'none';
})