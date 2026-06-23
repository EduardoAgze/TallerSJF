import threading
import time
from flask import Flask, render_template, jsonify, request
from logic.taller import Taller

app = Flask(__name__)

# ─── Instancia única del Taller (Model) ───
taller = Taller()

# ─── Hilo de fondo: avanza el tiempo cada segundo ───
def reloj():
    while True:
        taller.tick()
        time.sleep(1)

hilo_reloj = threading.Thread(target=reloj, daemon=True)
hilo_reloj.start()

# ─── 2.2 Ruta principal: entrega la página ───
@app.route("/")
def index():
    return render_template("index.html")

# ─── 2.3 Ruta de estado: devuelve JSON ───
@app.route("/estado")
def estado():
    return jsonify(taller.obtener_estado())

# ─── 2.4 Ruta para agregar un auto ───
@app.route("/agregar_auto", methods=["POST"])
def agregar_auto():
    datos = request.get_json()
    modelo = datos.get("modelo", "Desconocido")
    tiempo = datos.get("tiempo_reparacion", 5)

    exito = taller.agregar_auto(modelo, tiempo)

    if exito:
        return jsonify({"ok": True, "mensaje": f"{modelo} agregado a la cola"})
    else:
        return jsonify({"ok": False, "mensaje": "La cola está llena"}), 400

# ─── Arrancar el servidor ───
if __name__ == "__main__":
    app.run(debug=True)