from flask import Flask

# Nombre a desplegar
nombre = "Alejandro"

app = Flask(__name__)

@app.route('/')
def index():
    return f"
Bienvenido al portal universitario, {nombre}!
"

@app.route('/api/status')
def status():
return {"status": "ok", "entorno": "contenedor-docker", "version": "1.1.0"}

if name == 'main':
app.run(host='0.0.0.0', port=5000)
