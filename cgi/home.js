document.addEventListener('DOMContentLoaded',() => {
    const authButton = document.getElementById('auth-button');
    if(authButton) authButton.addEventListener('click', authButtonClick );
});

function authButtonClick() {
    const userLogin = document.getElementById('user-login');
    if(!userLogin) throw "Element #user-login not found";
    const userPassword = document.getElementById('user-password');
    if(!userPassword) throw "Element #user-password not found";
    const credentials = btoa( `${userLogin.value}:${userPassword.value}` )
    // fetch(`/auth?login=${userLogin.value}&password=${userPassword.value}`)
    fetch('/auth',{
        headers: {
            'Authorization': `Basic ${credentials}`,
        }
    })
    .then(r => r.text()).then(console.log);
    // console.log("Clicked");
}
