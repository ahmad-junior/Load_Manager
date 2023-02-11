// Variables
const firstName = document.getElementById('firstName'),
lastName = document.getElementById('lastName'),
email = document.getElementById('email_user'),
username = document.getElementById('user_name_unique'),
password = document.getElementById('password_user'),
passwordConfirm = document.getElementById('password_user_confirm'),
birthday = document.getElementById('birthday_user'),
submitBtn = document.getElementById('button_sinup');

// Reboot
const isNotReboot = document.getElementById('isNotReboot'),
isNotRebootOperandOne = document.getElementById('isNotRebootOperandOne'),
isNotRebootOperandTwo = document.getElementById('isNotRebootOperandTwo'),
isNotRebootSollution = document.getElementById('isNotRebootSollution');

// Set the values to the input fields
const oneO = Math.ceil(Math.random(1) * 5),
twoO = Math.ceil(Math.random(1) * 9),
resultO = oneO + twoO;

isNotRebootOperandOne.innerHTML = oneO;
isNotRebootOperandTwo.innerHTML = twoO;

// Password Validations
const pNumbers = document.getElementById('pNumbers'),
pLetters = document.getElementById('pLetters'),
pSLetters = document.getElementById('pSLetters'),
p8len = document.getElementById('p8len'),
showPasswod = document.getElementById('showPasswod');

// Check Password Validation
const checkPassword = () => {
    // Check Length
    if(password.value.length >= 8){
        p8len.style.color = '#00ff00';
    }else{
        p8len.style.color = '#ff0000';
    }

    // Check Numbers
    if(password.value.match(/[0-9]/)){
        pNumbers.style.color = '#00ff00';
    }else{
        pNumbers.style.color = '#ff0000';
    }

    // Check Capital Letters
    if(password.value.match(/[A-Z]/)){
        pLetters.style.color = '#00ff00';
    }else{
        pLetters.style.color = '#ff0000';
    }

    // Check Special Letters
    if(password.value.match(/[!@#$%^&*]/)){
        pSLetters.style.color = '#00ff00';
    }else{
        pSLetters.style.color = '#ff0000';
    }
}

// Check Password is Match
const checkPasswordMatch = () => {
    if(password.value === passwordConfirm.value){
        passwordConfirm.style.borderColor = '#00ff00';
    }else{
        passwordConfirm.style.borderColor = '#ff0000';
    }
}

// Call Password Validation
password.addEventListener('keyup', checkPassword);
passwordConfirm.addEventListener('keyup', checkPasswordMatch);

// Show Password
showPasswod.addEventListener('click', () => {
    if(password.type === 'password'){
        password.type = 'text';
        passwordConfirm.type = 'text';
        showPasswod.innerHTML = 'Hide Password';
    }else{
        password.type = 'password';
        passwordConfirm.type = 'password';
        showPasswod.innerHTML = 'Show Password';
    }
});

// Check Form Validation
const checkFormValidation = () => {
    if(firstName.value === '' || lastName.value === '' || email.value === '' || password.value === '' || passwordConfirm.value === '' || birthday.value === '' || username.value == "" || username.value.length <= 4 || isNotRebootSollution.value != resultO){
        submitBtn.style.opacity = '0.5';
        submitBtn.style.pointerEvents = 'none';
    }else{
        submitBtn.style.opacity = '1';
        submitBtn.style.pointerEvents = 'auto';
        submitBtn.style.backgroundColor = '#00ff00';
    }
}

// Call Form Validation
firstName.addEventListener('keyup', checkFormValidation);
lastName.addEventListener('keyup', checkFormValidation);
email.addEventListener('keyup', checkFormValidation);
username.addEventListener('keyup', checkFormValidation)
password.addEventListener('keyup', checkFormValidation);
passwordConfirm.addEventListener('keyup', checkFormValidation);
birthday.addEventListener('change', checkFormValidation);
isNotRebootSollution.addEventListener('keyup', checkFormValidation)
