from flask import render_template, request, redirect, url_for, flash
from models.todo import MinHeap, Auto

metodos = MinHeap()

def index():
    return render_template("index.html", autos=sorted(metodos.obtener_lista()))

def agregar():
    nombre = request.form.get("nombre")
    falla = request.form.get("falla")
    tiempo = int(request.form.get("tiempo"))
    
    if nombre and falla and tiempo:
        if not metodos.insertar(Auto(nombre, falla, tiempo)):
            flash('Cola llena, máximo 10 autos')
        else:
            flash('Auto agregado')
    
    return redirect(url_for("index"))

def siguiente():
    auto = metodos.extraer_min()
    if auto:
        flash(f'Auto procesado: {auto}')
    else:
        flash('No hay autos en la cola')
    
    return redirect(url_for("index"))

