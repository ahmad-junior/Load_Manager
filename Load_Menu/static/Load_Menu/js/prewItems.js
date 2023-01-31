    // Buttons
const   deleteBtnPI = document.getElementById('deleteBtnPI'),
        btnCancelPI = document.getElementById('btnCancelPI'),
        btnOKPI = document.getElementById('btnOKPI');
    
    // Contents
const popUpContent = document.getElementById('popUpContent');

    // Box
const popupBox = document.getElementById('popupBox');

    // Events
deleteBtnPI.addEventListener('click', () =>{
    popupBox.style.display = 'flex';
    popUpContent.innerText = "Are you sure to Delete this item Permanetly?";
})

btnCancelPI.addEventListener('click', () =>{
    popupBox.style.display = 'none';
})