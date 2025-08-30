document.addEventListener("DOMContentLoaded", () => {
    const busquedaInput = document.getElementById("busqueda");
    const resultadoDiv = document.getElementById("resultado");
    const infoDiv = document.getElementById("info");

    let datos = {};

    // ======================
    // Función para cargar datos según pestaña
    // ======================
    function cargarDatos(endpoint) {
        fetch(`http://127.0.0.1:5000/datos_${endpoint}`)
            .then(response => response.json())
            .then(jsonData => {
                datos = jsonData;
                busquedaInput.disabled = false;
                console.log(`Datos cargados de ${endpoint}:`, datos);
            })
            .catch(error => {
                console.error('Error al cargar los datos:', error);
            });
    }

    // ======================
    // Detectar pestaña seleccionada (incluye dropdowns)
    // ======================
    const menuLinks = document.querySelectorAll(".nav-link, .dropdown-item");
    menuLinks.forEach(link => {
        link.addEventListener("click", () => {
            const endpoint = link.getAttribute("data-endpoint");
            if (endpoint) {
                // resetear interfaz
                busquedaInput.value = "";
                resultadoDiv.style.display = "none";
                infoDiv.innerHTML = "";
                busquedaInput.disabled = true;

                // marcar pestaña activa
                menuLinks.forEach(l => l.classList.remove("active"));
                link.classList.add("active");

                // cargar datos
                if (endpoint === "general") {
                    // General combina todo → nuevo endpoint o lógica interna
                    fetch("http://127.0.0.1:5000/datos_general")
                        .then(res => res.json())
                        .then(jsonData => {
                            datos = jsonData;
                            busquedaInput.disabled = false;
                            console.log("Datos cargados de general:", datos);
                        })
                        .catch(err => console.error("Error en General:", err));
                } else {
                    cargarDatos(endpoint);
                }
            }
        });
    });

    // ======================
    // Búsqueda por código
    // ======================
    busquedaInput.addEventListener("input", () => {
        const valor = busquedaInput.value;
        const soloDigitos = valor.replace(/\D/g, ""); 

        if (soloDigitos.length >= 4) {
            let html = "";
            let totalResultados = 0;

            // Recorrer las hojas del Excel cargado
            for (let nombreHoja in datos) {
                const registros = datos[nombreHoja];
                const resultados = registros.filter(item =>
                    String(item['Codigos']).startsWith(soloDigitos)
                );

                if (resultados.length > 0) {
                    totalResultados += resultados.length;
                    html += `<h3 style="color:blue;">${nombreHoja}</h3>`;
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
                infoDiv.innerHTML = `<p style="color:red;">Código no encontrado en ninguna hoja.</p>`;
            }

        } else {
            resultadoDiv.style.display = "none";
            infoDiv.innerHTML = "";
        }
    });

    // ======================
    // Por defecto cargar pestaña general
    // ======================
    fetch("http://127.0.0.1:5000/datos_general")
        .then(res => res.json())
        .then(jsonData => {
            datos = jsonData;
            busquedaInput.disabled = false;
            console.log("Datos cargados de general:", datos);
        })
        .catch(err => console.error("Error en General inicial:", err));
});
