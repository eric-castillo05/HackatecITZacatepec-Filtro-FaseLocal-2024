import './App.css';
import Inicio from './componentes/Inicio'
import React from 'react';
import Plot from 'react-plotly.js';


function App() {
  return (
    <div className="App">

      <div className='contenedor-principal'>

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"></link>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"></link>
        
        <nav className="w-100 navbar navbar-expand-lg bg-secondary">

          <div className="container-fluid">
            <a className="navbar-brand text-light" href="#"><i class="bi bi-lungs-fill"></i>NetRunners</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
              <div className="navbar-nav">
                <a className="nav-link active text-light" aria-current="page" href="#">Acceso al Boot</a>
                <a className="nav-link text-light" href="#">Descargar registros</a>
              </div>
            </div>
          </div>
        </nav>

        <h1 className='my-4'>Día Nacional del Cáncer de Pulmón | 5 de abril</h1>
        <Inicio
          titulo='Cáncer de pulmón'
          subtitulo=''
          imagen="cancer"
          texto='El cáncer se produce cuando las células comienzan a crecer de manera 
        descontrolada en alguna parte del cuerpo y suelen propagarse a uno o 
        varios lugares del organismo. En la mayoría de los casos, las células 
        cancerosas forman un tumor.El cáncer de pulmón es un tipo de cáncer que 
        comienza en los pulmones, órganos esponjosos ubicados en el tórax que se 
        llenan de oxígeno al inhalar y al exhalar liberan dióxido de carbono. Este tipo de 
        cáncer puede comenzar en las células que envuelven los bronquios, los bronquiolos y/o 
        los alvéolos.'/>

        <Inicio
          titulo='Causas'
          subtitulo=''
          imagen="persona"
          texto='La principal causa del cáncer del pulmón es el tabaco. La Secretaría de 
      Salud estima que alrededor del 71% de los casos que desarrollan esta enfermedad tienen relación con el cigarro.
      De acuerdo con los Centros para el Control y Prevención de Enfermedades de Estados Unidos,
      las personas que fuman tienen entre 15 a 30 más probabilidades de contraer esta enfermedad o morir por esta causa con respecto a las personas que no fuman.
      También existen otros factores de riesgo, tales como:
      -Radioterapia previa: si la persona en cuestión ha estado expuesta a radioterapia en el pecho a causa de otro cáncer
      -Antecedentes familiares con cáncer de pulmón: las personas que han tenido algún familiar directo con este diagnóstico tienen mayor riego.'/>

        <Inicio
          titulo='Síntomas'
          subtitulo=''
          imagen="malo"
          texto='Este padecimiento no genera ningún síntoma al principio hasta que la enfermedad se encuentra avanzada. Los síntomas son:

      - Tos que no desaparece y empeora con el tiempo
      - Dolor constante en el pecho
      - Tos con expectoración y sangre
      - Falta de aire, silbidos al respirar o ronquera
      - Problemas repetidos por neumonía o bronquitis
      - Inflamación del cuello y la cara
      - Pérdida del apetito o pérdida de peso
      - Dificultad para respirar
      - Fatiga o debilidad'/>
      </div>

      <Plot
        data={[
          {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+markers',
            marker: {color: 'red'},
          },
          {type: 'bar', x: [1, 2, 3], y: [2, 5, 3]},
        ]}
        layout={ {width: 640, height: 480, title: 'A Fancy Plot'} }
      />
      
      
      
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
      

    </div>
  );
}

export default App;
