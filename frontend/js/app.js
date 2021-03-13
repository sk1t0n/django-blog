import '../sass/app.scss';

function clickNavbarBurger () {
  const navbarBurger = document.querySelector('.navbar-burger')
  const navbarMenu = document.getElementById('navbarMenu')
  navbarBurger.addEventListener('click', e => {
    navbarMenu.classList.toggle('is-active')
    navbarBurger.classList.toggle('is-active')
  })
}

window.addEventListener('load', event => {
  clickNavbarBurger()
})