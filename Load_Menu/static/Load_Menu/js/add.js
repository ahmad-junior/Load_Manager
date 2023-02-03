// Form Eelements
const id = document.getElementById('add_id'),
        name = document.getElementById('add_name'),
        number = document.getElementById('add_number'),
        price = document.getElementById('add_price'),
        gender = document.getElementById('add_gender'),
        date = document.getElementById('add_date'),
        loadType = document.getElementById('add_load_type'),
        operator = document.getElementById('add_operator'),
        address = document.getElementById('add_address'),
        shopKeeper = document.getElementById('add_shop_keeper');

// Add Button
const addBtn = document.getElementById('addSubmitBtn');

// Add Default Style -> Add Button
addBtn.style.opacity = '0.5';
addBtn.style.cursor = 'not-allowed';

// Check that input only have number or not
const containsOnlyNumbers = (str) => {
    return /^\d+$/.test(str);
}

// Check that Contains number or not
const isNumber = containsOnlyNumbers(number.value);

// Form Validation
const formValidation = () => {
    if(id.value == "" || name.value == "" || price.value <= 79 || (gender.value == "disabled" || loadType.value == "disabled" || operator.value == "disabled") || date.value == "" || loadType.value == "" || operator.value == "" || address.value == "" || shopKeeper.value == "" || number.value == "" || number.value.length < 11 || number.value.length > 11 || isNumber == true){
        addBtn.style.opacity = '0.5';
        addBtn.style.backgroundColor = '#ff0000';
        addBtn.style.cursor = 'not-allowed';
        addBtn.style.pointerEvents = 'none';
    } else {
        addBtn.style.opacity = '1';
        addBtn.style.backgroundColor = '#00ff00';
        addBtn.style.cursor = 'pointer';
        addBtn.style.pointerEvents = 'all';
    }
}

// Add Event Listener
id.addEventListener('keyup', formValidation);
name.addEventListener('keyup', formValidation);
number.addEventListener('keyup', formValidation);
price.addEventListener('keyup', formValidation);
gender.addEventListener('change', formValidation);
date.addEventListener('change', formValidation);
loadType.addEventListener('change', formValidation);
operator.addEventListener('change', formValidation);
address.addEventListener('keyup', formValidation);
shopKeeper.addEventListener('keyup', formValidation);

// ShowPopup
// Variables
const popupBox = document.getElementById('popupBox'),
    popUpContent = document.getElementById('popUpContent'),
    btnCancelPI = document.getElementById('btnCancelPI'),
    btnOkPI = document.getElementById('btnOkPI');

// Show Popup
addBtn.addEventListener('click', () => {
    popUpContent.innerText = "Are you sure you want to add this record?";
    popupBox.style.display = 'flex';
});

// Hide Popup
btnCancelPI.addEventListener('click', () =>{
    popupBox.style.display = 'none';
});
