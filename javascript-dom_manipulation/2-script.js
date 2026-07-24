const redheader = document.querySelector('#red_header');
const header = document.querySelector('header');
function addclass() {
  header.classList.add('red');
}

redheader.addEventListener('click', addclass);
