from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Cargar el modelo Joblib
model = joblib.load('model/model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Recibir la entrada de la solicitud (por ejemplo, datos para la predicción)
    data = request.get_json()

    # Preprocesar la entrada si es necesario

    # Generar una predicción usando el modelo cargado
    prediction = model.predict(data)

    # Retornar la predicción como JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
