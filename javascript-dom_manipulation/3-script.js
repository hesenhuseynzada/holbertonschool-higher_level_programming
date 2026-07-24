const header = document.querySelector('header');
const toggle_header = document.querySelector('#toggle_header');
function changeclass() {
    if (header.classList.contains('green')) {
        header.classList.toggle('red');
    }
    else if (header.classList.contains('red')) {
        header.classList.toggle('green');
    }
}
toggle_header.addEventListener('click', changeclass);
