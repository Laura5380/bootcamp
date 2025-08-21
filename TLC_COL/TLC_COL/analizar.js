// analizar.js
document.addEventListener("DOMContentLoaded", () => {
    const busquedaInput = document.getElementById("busqueda");
    const resultadoDiv = document.getElementById("resultado");
    const infoDiv = document.getElementById("info");

    let datos = {};

    // Cargar datos desde Flask
    fetch('http://127.0.0.1:5000/datos')
        .then(response => response.json())
        .then(jsonData => {
            datos = jsonData;
            busquedaInput.disabled = false;
            console.log("Datos cargados:", datos);
        })
        .catch(error => {
            console.error('Error al cargar los datos:', error);
        });

    busquedaInput.addEventListener("input", () => {
        const valor = busquedaInput.value;
        const soloDigitos = valor.replace(/\D/g, ""); // Solo números

        if (soloDigitos.length >= 4) {
            let html = "";
            let totalResultados = 0;

            // Recorrer todas las pestañas (hojas del Excel)
            for (let nombreHoja in datos) {
                const registros = datos[nombreHoja];

                // Filtrar coincidencias
                const resultados = registros.filter(item => 
                    String(item['Codigos']).startsWith(soloDigitos)
                );

                if (resultados.length > 0) {
                    totalResultados += resultados.length;

                    // Determinar si es Exportación o Importación
                    let tipo = nombreHoja.toUpperCase().includes("EX") ? "Exportación" :
                               nombreHoja.toUpperCase().includes("IM") ? "Importación" : "General";

                    html += `<h3 style="color:blue;">${tipo} - ${nombreHoja}</h3>`;

                    resultados.forEach(resultado => {
                        html += `<div style="margin-bottom:10px; padding:10px; border:1px solid #ccc; border-radius:5px;">`;
                        for (let key in resultado) {
                            html += `<p><strong>${key}:</strong> ${resultado[key]}</p>`;
                        }
                        html += `</div>`;
                    });
                }
            }

            if (totalResultados > 0) {
                resultadoDiv.style.display = "block";
                infoDiv.innerHTML = html;
            } else {
                resultadoDiv.style.display = "block";
                infoDiv.innerHTML = `<p style="color:red;">Código no encontrado en ninguna pestaña.</p>`;
            }

        } else {
            resultadoDiv.style.display = "none";
            infoDiv.innerHTML = "";
        }
    });
});
