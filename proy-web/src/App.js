import './App.css';
import Inicio from './componentes/Inicio'

function App() {
  return (
    <div className="App">
      <div className='contenedor-principal'>

      <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">
          <img src="/docs/4.0/assets/brand/bootstrap-solid.svg" width="30" height="30" alt=""/>
          </a>
          </nav>

      <h1>Día Nacional del Cáncer de Pulmón | 5 de abril </h1>
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
    </div>
  );
}

export default App;
