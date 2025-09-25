
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona o botão hamburger
    const menu = document.getElementById('menu');
    const menuToggle = document.createElement('button');
    menuToggle.className = 'menu-toggle';
    menuToggle.innerHTML = '☰';
    menuToggle.setAttribute('aria-label', 'Toggle menu');
    
    // Insere o botão antes do menu
    menu.parentNode.insertBefore(menuToggle, menu);
    
    // Função para toggle do menu
    menuToggle.addEventListener('click', function() {
        menu.classList.toggle('active');
        this.innerHTML = menu.classList.contains('active') ? '✕' : '☰';
    });
    
    // Fecha o menu quando clica em um link (mobile)
    const menuLinks = menu.querySelectorAll('a');
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                menu.classList.remove('active');
                menuToggle.innerHTML = '☰';
            }
        });
    });
    
    // Fecha o menu quando redimensiona para desktop
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            menu.classList.remove('active');
            menuToggle.innerHTML = '☰';
        }
    });
});

