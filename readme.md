# Taller Mecánico - Cola de Prioridad SJF

Simulador de taller mecánico que implementa una cola de prioridad usando **MinHeap** con el algoritmo **SJF (Shortest Job First)**. Los autos son atendidos según su tiempo de reparación, priorizando los trabajos más cortos.

## Características

- Cola de prioridad con capacidad máxima de 10 autos
- Algoritmo SJF: siempre atiende primero el auto con menor tiempo
- Desempate por orden de llegada (FIFO)
- Interfaz web con Flask
- Mensajes de feedback para el usuario

## Tecnologías

- **Backend**: Python, Flask
- **Estructura de datos**: MinHeap 
- **Frontend**: HTML, CSS, Jinja2

## Instalación local

```bash
# Clonar el repositorio
git clone https://github.com/EduardoAgze/TallerSJF.git
cd TallerSJF

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py