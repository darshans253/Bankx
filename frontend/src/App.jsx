import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
<<<<<<< HEAD
=======
import Header from './components/Header';
import Footer from './components/Footer';
>>>>>>> 255326d (Final)
import './App.css';

export default function App() {
  return (
    <BrowserRouter basename="/">
<<<<<<< HEAD
      <Routes>
        <Route path="/"          element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
=======
      <div className="app-layout">
        <Header />
        <div className="app-main">
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </div>
        <Footer />
      </div>
>>>>>>> 255326d (Final)
    </BrowserRouter>
  );
}

