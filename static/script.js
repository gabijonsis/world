
function openRegister() {
    var card = document.getElementById("cardy");
    card.style.transform = "rotateY(-180deg)"; 
    if(navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
        setTimeout(cardWaiting, 300)
        function cardWaiting() {
            document.getElementById("login").style.display = "none";     
        }
     }
}

function openLogin() {
    var card = document.getElementById("cardy");
    card.style.transform = "rotateY(0deg)";
    if(navigator.userAgent.toLowerCase().indexOf('firefox') > -1) {
        setTimeout(cardWaiting, 300)
        function cardWaiting() {
            document.getElementById("login").style.display = "block";
        }
    }
}
const menuBtn = document.querySelector(".hamburger");
const side = document.querySelector(".side");
let menuOpen = false;
menuBtn.addEventListener("click",() => {
    console.log("hh");
    if(!menuOpen) {
        side.setAttribute('style', 'display:inline !important');
        menuOpen = true;
    } 
    else {
        side.setAttribute('style', 'display:none !important');
        menuOpen = false;
    }
});