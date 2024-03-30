function togglePasswordVisibility() {
    var passwordField = document.getElementById("password");
    var icon = document.querySelector(".icon");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        icon.setAttribute("name", "eye-off");
    } else {
        passwordField.type = "password";
        icon.setAttribute("name", "eye");
    }
}

function redirect() {
    window.location.href = "../index_signup.html";
}
