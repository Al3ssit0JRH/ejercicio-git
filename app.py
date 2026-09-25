from flask import Flask

nombre = "Alejandro"

app = Flask("app_conflicto")

@app.route('/')
def index():
    return f"<h1>Bienvenido al portal universitario, {nombre}!</h1>"

@app.route('/api/status')
def status():
    return {"status": "ok", "entorno": "contenedor-docker", "version": "1.1.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
