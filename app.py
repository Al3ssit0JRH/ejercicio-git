from flask import Flask

nombre = "Alejandro"

app = Flask("app_error")

@app.route('/')
def index():
    return f"

Bienvenido al portal universitario, {nombre}!
"

if name == 'main':
app.run(host='0.0.0.0', port=5000)
