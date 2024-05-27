document.addEventListener('DOMContentLoaded', () => {
    const apiEndpoint = 'https://6654000b1c6af63f46761430.mockapi.io/index/UserPj';
    const tableBody = document.querySelector('#ninja-table tbody');
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
            errorMessage.textContent = error.message;
        }
    };

    const displayData = (data) => {
        const rows = data.map(ninja => `
            <tr>
                <td>${ninja.Nombre}</td>
                <td>${ninja.Clan}</td>
                <td>${ninja.Aldea}</td>
                <td>${ninja.Rango}</td>
            </tr>
        `).join('');
        tableBody.innerHTML = rows;
    };

    fetchData();
});
