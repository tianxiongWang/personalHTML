window.onload = function () {
    var welcomeDiv = document.getElementById('welcome')
    var timer1 = setInterval(welcomeRegister, 500);
    i = 0;

    function welcomeRegister() {
        for (k = 0; k < welcomeDiv.children.length; k++) {
            welcomeDiv.children[k].style.color = 'black';
        }
        welcomeDiv.children[i].style.color = 'white';
        i++;
        if (i > welcomeDiv.children.length - 1) {
            i = 0;
        }
    }
}