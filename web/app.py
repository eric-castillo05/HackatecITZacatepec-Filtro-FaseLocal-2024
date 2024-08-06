import redis
import pandas as pd
import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go

external_stylesheets = ['https://fonts.googleapis.com/css2?family=NombreDeLaFuente&display=swap']

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

df = recover(20)
x_features = [x for x in df.columns if x not in ['SEXO', 'EDAD']]
app = Dash(__name__, external_stylesheets=external_stylesheets)


pieChart = go.Figure(data=[go.Pie(labels=df['SEXO'], values=df['SEXO'].values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])


histo = go.Figure()
histo.add_trace(go.Histogram(x=df[df['SEXO']==1]))
histo.add_trace(go.Histogram(x=df[df['SEXO']==2]))
histo.update_layout(barmode='stack')


app.layout = html.Div([
    html.H1('NetRunners', style={'font-family': 'Roboto'}),
    html.Hr(),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    
    html.H1('Recuento por género para cada sintoma', style={'font-family': 'Roboto'}),
    dcc.Dropdown(
        id="dropdown",
        options=[{'label': i, 'value': i} for i in x_features],
        value="FUMADOR",
        clearable=False,
        style={'font-family': 'Roboto'}
    ),
    dcc.Graph(id="graph1"),

    html.Div([
        dcc.Graph(figure=histo)
    ])
])

@app.callback(
    Output("graph1", "figure"), 
    Input("dropdown", "value")
)
def update_bar_chart(y):
    fig = px.bar(df, x="SEXO", y=y, color="SEXO", barmode="group")
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    

    