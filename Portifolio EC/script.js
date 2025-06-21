// You can add JavaScript functionality here later.
// For example, smooth scrolling, interactive elements, etc.

document.addEventListener('DOMContentLoaded', () => {
    // Example: Highlight active navigation link
    const currentPath = window.location.pathname.split('/').pop();
    const navLinks = document.querySelectorAll('.navbar nav ul li a');

    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        }
    });
});