"""Controlador de Flask para la gestión de autos en la cola.

Este módulo define las rutas y las operaciones para agregar,
listar y procesar autos utilizando un MinHeap.
"""

from flask import render_template, request, redirect, url_for, flash
from models.todo import MinHeap, Auto

# Instancia global de la cola de autos.
metodos = MinHeap()


def index():
    """Mostrar la página principal con la lista de autos."""
    return render_template("index.html", autos=sorted(metodos.obtener_lista()))


def agregar():
    """Agregar un auto a la cola si los datos del formulario son válidos."""
    nombre = request.form.get("nombre")
    falla = request.form.get("falla")
    tiempo = int(request.form.get("tiempo"))

    if nombre and falla and tiempo:
        # Intentar insertar el auto en la cola de prioridad.
        if not metodos.insertar(Auto(nombre, falla, tiempo)):
            flash("Cola llena, máximo 10 autos")
        else:
            flash("Auto agregado")

    return redirect(url_for("index"))


def siguiente():
    """Procesar y eliminar el siguiente auto en la cola."""
    auto = metodos.extraer_min()

    if auto:
        flash(f"Auto procesado: {auto}")
    else:
        flash("No hay autos en la cola")

    return redirect(url_for("index"))

