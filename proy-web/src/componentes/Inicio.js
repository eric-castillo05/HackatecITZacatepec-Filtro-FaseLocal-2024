import React from 'react';
import '../hojas-de-estilo/Inicio.css'

function Inicion(props){
    return(
      <div className = 'contenedor-inicio'>
        <img className='imagen-inicio' 
        src={require(`../imagenes/pulmon-${props.imagen}.png`)}
        alt='Cancer-de-Pulmon'/>
      <div className = 'contenedor-inicio-texto'>
        <p className = 'info-titulo'>
          <b>{props.titulo}</b>
          </p>
        <p className = 'info-subtitulo'>{props.subtitulo}</p>
        <p className = 'info-texto'>{props.texto}</p>
      </div>
      </div>
    );    
}

export default Inicion;