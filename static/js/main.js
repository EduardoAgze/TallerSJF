// ─── 5.1 y 5.2: Preguntar el estado al Controller ─
function actualizarVista() {
    fetch("/estado")
        .then(respuesta => respuesta.json())
        .then(datos => {
            dibujarMecanico(datos.mecanico);
            dibujarCola(datos.cola);
        })
        .catch(error => console.error("Error al obtener estado:", error));
}

// ─── Dibujar el estado del mecánico ───
function dibujarMecanico(mecanico) {
    const contenedor = document.getElementById("info-mecanico");
    contenedor.className = ""; // Limpiar clases anteriores
    contenedor.innerHTML = ""; // Limpiar contenido

    if (mecanico.estado === "libre") {
        contenedor.classList.add("mecanico-libre");
        contenedor.textContent = `🔧 ${mecanico.nombre} está LIBRE`;
    } else {
        contenedor.classList.add("mecanico-ocupado");
        
        const auto = mecanico.auto_actual;
        const progreso = ((auto.tiempo_reparacion - mecanico.tiempo_restante) / auto.tiempo_reparacion) * 100;

        const texto = document.createElement("p");
        texto.textContent = `🔧 ${mecanico.nombre} reparando: ${auto.modelo} (${mecanico.tiempo_restante}s restantes)`;
        
        const barraContenedor = document.createElement("div");
        barraContenedor.className = "barra-contenedor";
        
        const barra = document.createElement("div");
        barra.className = "barra-progreso";
        barra.style.width = `${progreso}%`;
        barra.textContent = `${Math.round(progreso)}%`;
        
        barraContenedor.appendChild(barra);
        contenedor.appendChild(texto);
        contenedor.appendChild(barraContenedor);
    }
}

// ─── Dibujar la cola de autos ───
function dibujarCola(cola) {
    const contenedor = document.getElementById("lista-cola");
    contenedor.innerHTML = ""; // Limpiar lista
    contenedor.className = "";

    if (cola.length === 0) {
        contenedor.classList.add("lista-vacia");
        const item = document.createElement("li");
        item.textContent = "No hay autos en espera";
        contenedor.appendChild(item);
        return;
    }

    cola.forEach((auto, index) => {
        const item = document.createElement("li");
        item.className = "auto-cola";
        
        const nombre = document.createElement("span");
        nombre.innerHTML = `<strong>${index + 1}.</strong> ${auto.modelo}`;
        
        const tiempo = document.createElement("span");
        tiempo.className = "tiempo";
        tiempo.textContent = `${auto.tiempo_reparacion}s`;
        
        item.appendChild(nombre);
        item.appendChild(tiempo);
        contenedor.appendChild(item);
    });
}

// ─── 5.3: Avisar al Controller cuando el usuario hace clic ─
document.querySelectorAll(".btn-agregar").forEach(boton => {
    boton.addEventListener("click", () => {
        const tiempo = parseInt(boton.dataset.tiempo);
        const modelo = `Auto-${Date.now()}`;

        fetch("/agregar_auto", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ modelo, tiempo_reparacion: tiempo })
        })
        .then(respuesta => respuesta.json())
        .then(datos => {
            if (!datos.ok) alert(datos.mensaje);
        })
        .catch(error => console.error("Error al agregar auto:", error));
    });
});

// ── Iniciar ───
actualizarVista();
setInterval(actualizarVista, 1000);