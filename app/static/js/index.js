const nav_item = document.querySelectorAll(".nav-link");
const currentLoaction = location.href;


function ChangeActive(n) {
    nav_item[n].classList.add("active")
}


for (let i = 0; i < nav_item.length; i++) {
    if (nav_item[i].href === currentLoaction) {
        console.log(nav_item[i].href)
        ChangeActive(i)
    }
}