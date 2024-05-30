document.addEventListener('DOMContentLoaded', function() {
    const apiUrl = 'https://6654000b1c6af63f46761430.mockapi.io/index/JutsusGlobales';

    // Determinar la página actual
    const isKatonPage = document.body.classList.contains('katon-page');
    const isFutonPage = document.body.classList.contains('futon-page');
    const isDotonPage = document.body.classList.contains('doton-page');
    const isRaitonPage = document.body.classList.contains('raiton-page');
    const isSuitonPage = document.body.classList.contains('suiton-page');
    const isTaijutsuPage = document.body.classList.contains('taijutsu-page');

    // Función para convertir el rango a un valor numérico para ordenar
    function rangoValor(rango) {
        const rangos = { "D": 1, "C": 2, "C+":3, "B": 4,"B+":5, "A": 6, "S": 7 };
        return rangos[rango] || 0;
    }

    // Crear los recuadros de jutsus
    function crearRecuadroJutsu(jutsu) {
        const container = document.querySelector('.jutsu-container');
        const jutsuBox = document.createElement('div');
        jutsuBox.classList.add('text-box');
        
        jutsuBox.innerHTML = `
            <h2>${jutsu.Nombre}</h2>
            <p>Rango : ${jutsu.Rango}</p>
            <p>Sellos : ${jutsu.Sellos}</p>
            <p>${jutsu.Descripción}</p>
            <a href="${jutsu.Wiki}">Wiki</a>
        `;
        
        container.appendChild(jutsuBox);
    }

    // Función para obtener los datos de la API y agregar los jutsus al contenedor
    function cargarJutsus(apiUrl, elemento) {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const jutsusFiltrados = data.filter(jutsu => jutsu.Elemento === elemento);
                jutsusFiltrados.sort((a, b) => rangoValor(a.Rango) - rangoValor(b.Rango));
                jutsusFiltrados.forEach(crearRecuadroJutsu);
            })
            .catch(error => console.error('Error al obtener los datos:', error));
    }

    // Cargar los jutsus correspondientes según la página
    if (isKatonPage) {
        cargarJutsus(apiUrl, 'Katon');
    } else if (isFutonPage) {
        cargarJutsus(apiUrl, 'Futon');
    } else if (isDotonPage) {
        cargarJutsus(apiUrl, 'Doton');
    } else if (isRaitonPage) {
        cargarJutsus(apiUrl, 'Raiton');
    } else if (isSuitonPage) {
        cargarJutsus(apiUrl, 'Suiton');
    } else if (isTaijutsuPage) {
        cargarJutsus(apiUrl, 'Taijutsu');
    } else {
        console.error('Página desconocida. No se pueden cargar los datos de los jutsus.');
    }
});
