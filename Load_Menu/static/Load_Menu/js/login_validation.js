// Variables
const userNameLogin = document.getElementById('userNameLogin'),
userPasswordLogin = document.getElementById('userPasswordLogin'),
SHPassword = document.getElementById('SHPassword'),
submitButtonLogin = document.getElementById('submitButtonLogin');

// Reboot
const isNotReboot = document.getElementById('isNotReboot'),
isNotRebootOperandOne = document.getElementById('isNotRebootOperandOne'),
isNotRebootOperandTwo = document.getElementById('isNotRebootOperandTwo'),
isNotRebootSollution = document.getElementById('isNotRebootSollution');

// Set the values to the input fields
const setPuzzle = () =>{
    const oneO = Math.ceil(Math.random(1) * 5),
    twoO = Math.ceil(Math.random(1) * 9);

    isNotRebootOperandOne.value = oneO;
    isNotRebootOperandTwo.value = twoO;
    isNotRebootSollution.value = "";
}
setPuzzle();
// Refresh the puzzle
const rSHBtn = document.getElementById('refreshPuzzle');
rSHBtn.addEventListener('click', setPuzzle);
// Check puzzle solution
const resultO = () =>{
    const result = parseInt(isNotRebootOperandOne.value) + parseInt(isNotRebootOperandTwo.value);
    return result;
}

// Events
// Show Password
SHPassword.addEventListener('click', () => {
    if(SHPassword.innerHTML == "Show"){
        userPasswordLogin.type = "text";
        SHPassword.innerHTML = "Hide";
    } else{
        userPasswordLogin.type = "password";
        SHPassword.innerHTML = "Show";
    }
});

// Submit Button And Form Validation
const formValidationLogin = () => {
    if(userPasswordLogin.value == "" || userPasswordLogin.value.length < 8 || userNameLogin.value == "" || isNotRebootSollution.value != resultO()){
        submitButtonLogin.style.pointerEvents = "none";
        submitButtonLogin.style.opacity = 0.5;
        submitButtonLogin.style.background = "#ff0000";
    } else{
        submitButtonLogin.style.pointerEvents = "all";
        submitButtonLogin.style.opacity = 1;
        submitButtonLogin.style.background = "#00ff00";
    }
};
// Call the Validation Function
userNameLogin.addEventListener('keyup', formValidationLogin);
userPasswordLogin.addEventListener('keyup', formValidationLogin);
isNotRebootSollution.addEventListener('keyup', formValidationLogin);
rSHBtn.addEventListener('click', formValidationLogin);