import { useState } from 'react';
import './App.css';
import Nav from '../components/Nav.jsx'
import Footer from '../components/Footer.jsx'
import {Routes, Route} from 'react-router-dom'
import Home from '../pages/Home.jsx'
import Contact from '../pages/Contact.jsx'




function App() {
  

  return (
    <>
    <Nav></Nav>
    <main className="main-content">
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/contact' element={<Contact/>} />
      </Routes>
    </main>

    <Footer></Footer>
    
    </>
  );
}

export default App;
