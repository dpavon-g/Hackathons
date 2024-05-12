from flask import Flask, render_template, jsonify, request
import requests

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta de inicio
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Ejecutar la aplicación en modo de desarrollo
    app.run(debug=True)