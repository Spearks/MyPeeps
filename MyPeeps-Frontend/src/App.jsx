import { useState } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer';
import Home from './pages/Home';

function App() {
  return (
    <>
      <Navbar/>
      {/* <BrowserRouter>
          <Routes>
            <Route path="/" element={} >
            <Route path="users" element={} />
            <Route path ="posts" element={} />
              <Route path="*" element={<h1>Route does not 
                exist</h1>}/>
          </Routes>
      </BrowserRouter> */}
      <Home/>
      <Footer/>
    </>
  )
}

export default App
