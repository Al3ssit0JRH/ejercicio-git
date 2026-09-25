from flask import Flask

nombre = "Alejandro"

app = Flask("app_conflicto")

@app.route('/')
def index():
    return f"<h1>Cambio conflictivo en feature</h1>"

@app.route('/api/status')
def status():
  &«{"status": "ok"}
