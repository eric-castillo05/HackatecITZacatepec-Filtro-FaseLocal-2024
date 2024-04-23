from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Cargar el modelo desde el archivo .joblib
model = joblib.load('model/model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos de la solicitud POST
    data = request.get_json()
    print(f"Datos recibidos: {data}")

    # Convertir los valores booleanos a números
    for key, value in data.items():
        if isinstance(value, bool):
            data[key] = 1 if value else 0

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame([data])

    # Realizar la conversión de valores para las columnas específicas
    columns_to_convert = ['Sexo', 'Edad']
    for column in df.columns:
        if column not in columns_to_convert:
            df[column] = df[column].map({1: False, 2: True})

    # Preprocesar los datos adicionales si es necesario
    # ...

    # Generar una predicción usando el modelo cargado
    prediction = model.predict(df.values)

    # Retornar la predicción como JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
