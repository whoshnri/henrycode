import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  const click = (name) => {
    console.log('hey ' + name)
    document.querySelector('.btn2').value = 'hey'

} 
  const click2 = (e) => {
    console.log(e.target)
} 
  const click3 = (e) => {
    console.log(e.target.innerText)
} 


const double = () => {
  console.log('you double clicked it')
}

const hover = () => {
  console.log('hovered')
}


  return (
    <>
      

    
      
      
    </>
  )
}

export default App
