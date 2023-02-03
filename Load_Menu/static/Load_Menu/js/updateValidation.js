// Input Search Box
const inputItem = document.getElementById('inputItem');

// Button
const submitBtnBoth = document.getElementById('submitBtnBoth');

// Check that input only have number or not
const containsOnlyNumbers = (str) => {
    return /^\d+$/.test(str);
}

// Validation
const formValidation = () => {
    if(inputItem.value == "" || inputItem.value.length < 11 || inputItem.value.length > 11){
        submitBtnBoth.style.opacity = '0.5';
        submitBtnBoth.style.cursor = 'not-allowed';
        submitBtnBoth.style.backgroundColor = '#ff0000';
    }
    else if(containsOnlyNumbers(inputItem.value)){
        submitBtnBoth.style.opacity = '1';
        submitBtnBoth.style.backgroundColor = '#00ff00';
        submitBtnBoth.style.cursor = 'pointer';
        submitBtnBoth.style.pointerEvents = 'all';
    }
    else{
        submitBtnBoth.style.opacity = '0.5';
        submitBtnBoth.style.cursor = 'not-allowed';
        submitBtnBoth.style.backgroundColor = '#0000ff';
    }
}

// Add events
inputItem.addEventListener('keyup', formValidation);