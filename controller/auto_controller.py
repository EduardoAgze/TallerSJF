from flask import render_template, request, redirect, url_for, flash
from models.todo import Min_Heap, Auto

metodos = Min_Heap()

def index():
    return render_template("index.html", autos=metodos.obtener_lista())

def agregar():
    nombre = request.form.get("nombre")
    falla = request.form.get("falla")
    tiempo = int(request.form.get("tiempo"))
    
    if nombre and falla and tiempo:
        if not metodos.agregar_auto(nombre, falla, tiempo):
            flash('Cola llena, máximo 10 autos')
        else:
            flash('Auto agregado')
    
    return redirect(url_for("index"))

