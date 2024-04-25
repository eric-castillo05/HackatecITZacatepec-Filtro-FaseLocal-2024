import redis
import pandas as pd
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

r = redis.Redis(host='redis-10364.c325.us-east-1-4.ec2.cloud.redislabs.com',
  port=10364,
  password='9oxEjbS4slyRNmxknio5Ryi8UaasqLYC')

def recover(tamano):
    data = []  # Lista para almacenar los datos recuperados
    
    lastreg = r.keys("*")  # Obtener todas las claves
    
    for i in range(tamano):  # Iterar sobre las claves hasta el tamaño especificado
        key = lastreg[i].decode('utf-8')  # Convertir la clave bytes a cadena
        
        vals = r.hvals(key)  # Obtener los valores asociados con la clave
        
        # Crear un diccionario para almacenar los datos
        record = {'key': key,'values': [val.decode('utf-8') for val in vals]}
        
        data.append(record)  # Agregar el diccionario a la lista de datos
        
    # Crear un DataFrame a partir de la lista de datos
    df = pd.DataFrame(data)
    df.columns = ['column2','column3']
    df_segunda_columna = pd.DataFrame(df['column3'].tolist(), columns=['SEXO', 'EDAD', 'FUMADOR', 'DEDOS_AMARILLOS', 'ANSIEDAD', 'PRESION_DE_GRUPO', 'ENFERMEDAD_CRONICA', 'FATIGA', 'ALERGIA', 'SIBILANCIAS', 'CONSUMO_ALCOHOL', 'TOS', 'DIFICULTAD_RESPIRAR', 'DIFICULTAD_TRAGAR', 'DOLOR_PECHO', 'CANCER_PULMON'])
    return df_segunda_columna

# Ejemplo de uso
length=r.keys("*")
#tamano=len(length)

df = recover(5)
print(df.head())

    

    