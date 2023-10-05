import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer';
import Home from './pages/Home';
import LoginForm from './pages/LoginForm';

function App() {
  return (
    <Router>
      <div>
      <Navbar/>
      <Routes>
        <Route exact path="/" element={<Home/>} />
        <Route exact path="/login" element={<LoginForm/>} />
      </Routes>

      <Footer/>
      </div>
    </Router>
  )
}

export default App
