import { useState } from 'react';
import './App.css'
import Home from '../pages/Home.jsx'
import FavPage from '../pages/FavPage.jsx'
import Nav from './components/Navbar.jsx'
import {Routes, Route} from 'react-router-dom'




function App() {


  return (
    <>
      <Nav></Nav>
      <main className='main-content'>
        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/favourites' element={<FavPage/>}/>
        </Routes>


      </main>


    
    </>
  )
}

export default App























// function Card(){
//   const [color, setColor] = useState('white')
  
//   function loadcolour(){
//     const color_new = document.querySelector('.color-change').value
//     if  (color_new != ''){
//       setColor(color_new);
//       inputElement.value = '';
//     }

//   }
  

//   return (
//     <div className="card">
//       <div className="box"  style={{backgroundColor: color}} ></div>
//       <input type="text" className='color-change'/>
//       <button type="button" className='button' onClick={loadcolour}>Enter</button>
//     </div>

//   )
// }

// function Text(){
//   return (
//       <h1>Color Picker</h1>
//   )
// }