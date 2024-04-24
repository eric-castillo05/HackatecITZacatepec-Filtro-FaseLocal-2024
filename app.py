from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import uuid
import redis

app = Flask(__name__)

# Cargar el modelo desde el archivo .joblib
model = joblib.load('models/model.joblib')
r = redis.Redis(
  host='redis-10364.c325.us-east-1-4.ec2.cloud.redislabs.com',
  port=10364,
  password='9oxEjbS4slyRNmxknio5Ryi8UaasqLYC')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos de la solicitud POST
    data = request.get_json()
    print(f"Datos recibidos: {data}")

    nreg = str(uuid.uuid4())

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame([data])

    # Realizar la conversión de valores para las columnas específicas
    columns_to_convert = ['Sexo', 'Edad']
    for column in df.columns:
        if column not in columns_to_convert:
            df[column] = df[column].map({1: False, 2: True})

    # Generar una predicción usando el modelo cargado
    prediction = model.predict(df)
    r.hset(nreg, "sexo", data['Sexo'])
    r.hset(nreg, "edad", data['Edad'])
    r.hset(nreg, "fumador", data['Fumador'])
    r.hset(nreg, "dedos_amarillos", data['dedos amarillos'])
    r.hset(nreg, "ansiedad", data['Ansiedad'])
    r.hset(nreg, "presion_de_grupo", data['presion de grupo'])
    r.hset(nreg, "enfermedad_cronica", data['enfermedad cronica'])
    r.hset(nreg, "fatiga", data['fatiga'])
    r.hset(nreg, "alergia", data['Alergia'])
    r.hset(nreg, "sibilancias", data['Sibilancias'])
    r.hset(nreg, "consumo_alcohol", data['Consumo Alcohol'])
    r.hset(nreg, "tos", data['Tos'])
    r.hset(nreg, "dificultad_respirar", data['Dificultad respirar'])
    r.hset(nreg, "dificultad_tragar", data['Dificultad tragar'])
    r.hset(nreg, "dolor_en_pecho", data['Dolor en pecho'])
    r.hset(nreg, "cancer_pulmon", int(prediction[0]))

    # Retornar la predicción como JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)