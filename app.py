from flask import Flask, render_template, request, redirect, flash
from models.todo import MinHeap, Auto

app = Flask(__name__)

# El heap vive aquí (en memoria, mientras corre la app)
cola = MinHeap()

@app.route('/')
def index():
    
    lista= cola.obtener_lista()
    autos_ordenados = sorted(lista)
    return render_template('index.html', autos=autos_ordenados)




@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    falla = request.form['falla']
    tiempo = int(request.form['tiempo'])

    auto = Auto(nombre, falla, tiempo)
    cola.insertar(auto)

if __name__ == '__main__':
    app.run(debug=True)