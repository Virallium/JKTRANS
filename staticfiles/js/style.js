function AOS_anim(){
    
        document.addEventListener('DOMContentLoaded', function() {
            // Initialisation d'AOS
            AOS.init({
                duration: 800,
                once: false,
                mirror: true
            });

            // Initialisation de Swiper
            const swiper = new Swiper('.mySwiper', {
                effect: 'coverflow',
                grabCursor: true,
                centeredSlides: true,
                slidesPerView: 'auto',
                coverflowEffect: {
                    rotate: 30,
                    stretch: 0,
                    depth: 100,
                    modifier: 1,
                    slideShadows: true,
                },
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
            });
        });
}
AOS_anim();


function menu_toggle(){
    const menu_bar = document.querySelector('#menu');
        const nav = document.querySelector('nav');
        const rgba = document.querySelector('.rgba');

        if (menu_bar && nav && rgba) {
            menu_bar.addEventListener('click', () => {
                nav.classList.toggle('active');
                rgba.classList.toggle('active');
            });

            rgba.addEventListener('click', () => {
                nav.classList.remove('active');
                rgba.classList.remove('active');
            });

            document.querySelectorAll('nav a').forEach(link => {
                link.addEventListener('click', () => {
                    nav.classList.remove('active');
                    rgba.classList.remove('active');
                });
            });
        }
}
menu_toggle();

function scroll_nav(){
    const header = document.querySelector('.header');
    const scrollThreshold = 150;
    window.addEventListener('scroll', ()=>{
        if (window.scrollY > scrollThreshold){
            header.classList.add('scrolled')
        }
        else{
            header.classList.remove('scrolled')
        }
    })
}
scroll_nav();