document.addEventListener('DOMContentLoaded', () => {
    const apiEndpoint = 'https://6654000b1c6af63f46761430.mockapi.io/index/UserPj';
    const primeraGeneracionTable = document.querySelector('#ninja-table-primerageneracion tbody');
    const segundaGeneracionTable = document.querySelector('#ninja-table-segundageneracion tbody');
    const terceraGeneracionTable = document.querySelector('#ninja-table-tercerageneracion tbody');
    const errorMessage = document.getElementById('error-message');

    const fetchData = async () => {
        try {
            const response = await fetch(apiEndpoint);
            if (!response.ok) {
                throw new Error(`Error en la solicitud: ${response.statusText}`);
            }
            const data = await response.json();
            displayData(data);
        } catch (error) {
            console.error('Error al obtener los datos:', error);
        }
    };

    const displayData = (data) => {
        data.forEach(ninja => {
            const newRow = `
                <tr>
                    <td>${ninja.Nombre}</td>
                    <td>${ninja.Clan}</td>
                    <td>${ninja.Aldea}</td>
                    <td>${ninja.Rango}</td>
                </tr>
            `;

            if (ninja.Generacion === "1") {
                primeraGeneracionTable.innerHTML += newRow;
            } else if (ninja.Generacion === "2") {
                segundaGeneracionTable.innerHTML += newRow;
            }else if (ninja.Generacion === "3") {
                terceraGeneracionTable.innerHTML += newRow;
            }
        });
    };

    fetchData();
});

