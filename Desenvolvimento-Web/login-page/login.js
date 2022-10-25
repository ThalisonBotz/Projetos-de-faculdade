function loginCheck () {
    const btn = document.getElementById('btn');
    const email = document.getElementById('email');
    const emailError = document.getElementById('email-error');
    const passError = document.getElementById('pass-error');
    const pass = document.getElementById('pass');

    email.addEventListener('blur', function(){
        if (this.value.indexOf('@')> - 1){
            console.log('Valid Email');
            emailError.style.display = "none";
        } else {
            console.log('Invalid Email');
            emailError.style.display = "block";
        }
    });
    pass.addEventListener('blur', function(){
        if (this.value.length > 10) {
            console.log('Valid Password');
            passError.style.display = "none";
        } else {
            console.log('Invalid, Small Password');
            passError.style.display = "block";
        }
    });
    btn.addEventListener('click', function(e){
        if (pass.value.length > 10) {
            if (email.value.indexOf('@') > - 1) {
                const user = email.value;
                const userPass = pass.value;
                console.log('User: ' + user)
                console.log('Password: ' + userPass)
                alert('Successful Login' + ' welcome: ' + user);
            } else {
                alert('Invalid Email');
                e.preventDefault();
            }
        } else {
            alert('Invalid, Small Password');
            e.preventDefault();
        };
    });
}
window.addEventListener("load", function(e){
    loginCheck();
})
