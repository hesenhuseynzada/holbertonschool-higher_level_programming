const update_header = document.querySelector('#update_header');
const header = document.querySelector("header")

function updateheader(){
    header.textContent("New Header!!!")
}
update_header.addEventListener("click", update_header)
