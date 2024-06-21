document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuOpenIcon = mobileMenuButton.querySelector('svg:nth-child(1)');
    const menuCloseIcon = mobileMenuButton.querySelector('svg:nth-child(2)');
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = userMenuButton.nextElementSibling;
  
    mobileMenuButton.addEventListener('click', () => {
      const isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
      mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
      mobileMenu.classList.toggle('hidden');
      menuOpenIcon.classList.toggle('hidden');
      menuCloseIcon.classList.toggle('hidden');
    });

  
    userMenuButton.addEventListener('click', () => {
      userMenu.classList.toggle('hidden');
    });
  
    document.addEventListener('click', (event) => {
      if (!userMenuButton.contains(event.target) && !userMenu.contains(event.target)) {
        userMenu.classList.add('hidden');
      }
    });
  });

  
  