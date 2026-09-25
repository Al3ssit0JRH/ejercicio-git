from flask import Flask

# Nombre a desplegar
nombre = "Alejandro"

app = Flask(__name__)

@app.route('/')
def index():
    return f"
ienvenido al portal universitario, {nombre}!
"

if name == 'main':
app.run(host='0.0.0.0', port=5000)

