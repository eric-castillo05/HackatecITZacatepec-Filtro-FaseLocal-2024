from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import uuid
import redis


#Acceder a la BD
r = redis.Redis(
  host='redis-10364.c325.us-east-1-4.ec2.cloud.redislabs.com',
  port=10364,
  password='9oxEjbS4slyRNmxknio5Ryi8UaasqLYC')

# Abrir el csv
df = pd.read_csv('datasets\respuestas_filtered.csv')
print(df.head)
for row in df.columns:
    nreg = str(uuid.uuid4())
    data = {
            'Sexo': row[0],
            'Edad': row[1],
            'Fumador': row[2],
            'Dedos Amarillos': row[3],
            'Ansiedad': row[4],
            'Presion de grupo': row[5],
            'Enfermedad cronica': row[6],
            'Fatiga': row[7],
            'Alergia': row[8],
            'Sibilancias': row[9],
            'Consumo Alcohol': row[10],
            'Tos': row[11],
            'Dificultad respirar': row[12],
            'Dificultad tragar': row[13],
            'Dolor en pecho': row[14],
            'Cancer de pulmon': row[15]
        }

    # Iteramos por columna 
    for row in df.columns:
        # Convertir los datos a un diccionario 
        data = {
            'Sexo': row[0],
            'Edad': row[1],
            'Fumador': row[2],
            'Dedos Amarillos': row[3],
            'Ansiedad': row[4],
            'Presion de grupo': row[5],
            'Enfermedad cronica': row[6],
            'Fatiga': row[7],
            'Alergia': row[8],
            'Sibilancias': row[9],
            'Consumo Alcohol': row[10],
            'Tos': row[11],
            'Dificultad respirar': row[12],
            'Dificultad tragar': row[13],
            'Dolor en pecho': row[14],
            'Cancer de pulmon': row[15]
        }


        # Extraer valores
        Sexo = data.get('Sexo')
        Edad = data.get('Edad')
        Fumador = data.get('Fumador')
        Dedos= data.get('Dedos Amarillos')
        Ansiedad = data.get('Ansiedad')
        Presion = data.get('Presion de grupo')
        Enfermedad = data.get('Enfermedad')
        Fatiga = data.get('Fatiga')
        Alergia = data.get('Alergia')
        Sibilancias = data.get('Sibilancias')
        Alcohol = data.get('Consumo Alcohol')
        Tos = data.get('Tos')
        Difrespirar = data.get('Dificultad respirar')
        Diftragar = data.get('Dificultar tragar')
        DolorPecho = data.get('Dolor en pecho')
        Cancer = data.get('Cancer de pulmon')


        # Almacenar valores individuales
        r.hset(nreg, row[0] + ':Sexo', Sexo)
        r.hset(nreg, row[0] + 'Edad', Edad)
        r.hset(nreg, row[0] + ':Fumador', Sexo)
        r.hset(nreg, row[0] + 'Dedos amarillos', Dedos)
        r.hset(nreg, row[0] + ':Ansiedad', Ansiedad)
        r.hset(nreg, row[0] + 'Presion de grupo', Presion)
        r.hset(nreg, row[0] + ':Sexo', Sexo)
        r.hset(nreg, row[0] + 'Edad', Edad)
        r.hset(nreg, row[0] + ':Sexo', Sexo)
        r.hset(nreg, row[0] + 'Edad', Edad)

 
