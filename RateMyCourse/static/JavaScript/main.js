/* Show Menu */
const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId), 
    nav = document.getElementById(navId)

    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show-menu')
        })
    }
}
showMenu('nav-toggle', 'nav-menu')

/* Remove Menu Mobile */
const navLink = document.querySelectorAll('.nav__link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/* Scroll Sections Active Link */
const sections = document.querySelectorAll('section[id]')

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight 
        const sectionTop = current.offsetTop - 120
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav__menu a[href*=' + sectionId+ ']').classList.add('active-link')
        }else{
            document.querySelector('.nav__menu a[href*=' + sectionId+ ']').classList.remove('active-link')
        }
    })
}

window.addEventListener('scroll', scrollActive)

/* Change Background Header */
function scrollHeader(){
    const header = document.getElementById('header')
    const scrollThreshold = window.innerWidth < 576 ? 1267 : 750;
    //if(this.scrollY >= 750) header.classList.add('scroll-header'); else header.classList.remove('scroll-header')

    if (this.scrollY >= scrollThreshold) {
      header.classList.add('scroll-header');
    } else {
      header.classList.remove('scroll-header');
  }
}

window.addEventListener('scroll', scrollHeader)

/* Show Scroll Top */
function scrollTop(){
    const scrollTop = document.getElementById('scroll-top')
    if(this.scrollY >= 560) scrollTop.classList.add('show-scroll'); else scrollTop.classList.remove('show-scroll')
}

window.addEventListener('scroll', scrollTop)

/* Link active portfolio */
const linkPortfolio = document.querySelectorAll('.portfolio__item')

function activePortfolio(){
    if(linkPortfolio){
        linkPortfolio.forEach(l => l.classList.remove('active-portfolio'))
        this.classList.add('active-portfolio')
    }
}
linkPortfolio.forEach(l => l.addEventListener('click', activePortfolio))

/* GSAP Annimation */
gsap.from('.home__img',{opacity: 0, duration: 1, delay:.25, x:60})
gsap.from('.home__data',{opacity: 0, duration: 1, delay:.3, y:25})
gsap.from('.home__greeting, .home__name, .home__profession',{opacity: 0, duration: 1, delay:.25, y:25, ease:'expo.out', stagger:.2})

gsap.from('.nav__logo, .nav__toggle',{opacity: 0, duration: 1, delay:.35, y:25, ease:'expo.out', stagger:.2})
gsap.from('.nav__item',{opacity: 0, duration: 1, delay:.35, y:25, ease:'expo.out', stagger:.2})
gsap.from('.home__social-icon',{opacity: 0, duration: 1, delay:.45, y:25, ease:'expo.out', stagger:.2})

gsap.from('.ratings',{opacity: 0, duration: 1, delay:.25, x:-15})
gsap.from('.ratings__stars',{opacity: 0, duration: 1, delay:.25, x:-15})

gsap.from('.graph',{opacity: 0, duration: 1, delay:.25, x:-15})
gsap.from('.graph__bar',{opacity: 0, duration: 1, delay:.25, x:-60})

/* Sign-Up and Log-In Pop-Up */
function openLoginModal() {
  document.getElementById("loginModal").style.display = "block";
}

function openSignupModal() {
  document.getElementById("signupModal").style.display = "block";
}

function closeModal() {
  document.getElementById("loginModal").style.display = "none";
  document.getElementById("signupModal").style.display = "none";
}


/* Home Annimation */
document.querySelector('.home').classList.add('show');
document.querySelector('.result').classList.add('show');  