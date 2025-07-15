import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Header from './components/Header';
import Footer from './components/Footer';
import ProtectedRoute from './components/ProtectedRoute';
import './App.css';
import Admin from "./pages/Admin";

export default function App() {
  return (
    <BrowserRouter basename="/">
      <div className="app-layout">
        <Header />
        <div className="app-main">
          <Routes>
            <Route path="/" element={<Login />} />
            <Route
              path="/dashboard"
              element={
                <ProtectedRoute>
                  <Dashboard />
                </ProtectedRoute>
              }
            />
            <Route path="/admin" element={<Admin />} /> {/* 👈 Unprotected route */}
          </Routes>
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
}
