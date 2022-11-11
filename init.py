from flask import Flask

app = Flask(__name__)


# Validar que el servicio está arriva
@app.route('/')
def index():
    return "Servidor en Ejecución"

#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