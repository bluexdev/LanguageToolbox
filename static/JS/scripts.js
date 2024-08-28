document.addEventListener('DOMContentLoaded', (event) => {
    const darkModeToggle = document.getElementById('toggle-dark-mode');
    const darkModeIcon = document.getElementById('dark-mode-icon');
    const lightModeIcon = document.getElementById('light-mode-icon');

    darkModeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        
        // Cambiar la visibilidad de los íconos
        if (document.body.classList.contains('dark-mode')) {
            darkModeIcon.style.display = 'none';
            lightModeIcon.style.display = 'inline';
        } else {
            darkModeIcon.style.display = 'inline';
            lightModeIcon.style.display = 'none';
        }
        
        // Guardar la preferencia en localStorage
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    });

    // Verificar la preferencia guardada al cargar la página
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        darkModeIcon.style.display = 'none';
        lightModeIcon.style.display = 'inline';
    }
});
