from flask import Flask

nombre = "Alejandro"

app = Flask("app_error")

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
