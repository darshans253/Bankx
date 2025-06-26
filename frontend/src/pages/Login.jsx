import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import '../App.css';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [msg, setMsg] = useState('');
  const nav = useNavigate();

  const call = async (path) => {
    try {
      const { data } = await api.post(`/user/${path}`, { email, password });
<<<<<<< HEAD
      setMsg(JSON.stringify(data));
      if (path === 'login') nav('/dashboard', { state: { email } });
    } catch (e) {
      setMsg(e.response?.data?.detail ?? e.message);
=======

      if (path === 'register') {
        setMsg('✅ Account successfully created.');
      } else if (path === 'login') {
        setMsg('✅ Login successful.');
        nav('/dashboard', { state: { email } });
      }
    } catch (e) {
      const err = e.response?.data?.detail ?? e.message;

      if (path === 'register' && err === 'Email already registered') {
        setMsg('❌ Account already exists. Try logging in.');
      } else if (path === 'login' && err === 'Invalid credentials') {
        setMsg('❌ Incorrect email or password.');
      } else {
        setMsg(`❌ ${err}`);
      }
>>>>>>> 255326d (Final)
    }
  };

  return (
    <div className="card">
<<<<<<< HEAD
      <h2>BankX Auth</h2>
      <input placeholder="Email"    value={email}
             onChange={e => setEmail(e.target.value)} />
      <input placeholder="Password" type="password" value={password}
             onChange={e => setPassword(e.target.value)} />
=======
      <input
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        placeholder="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

>>>>>>> 255326d (Final)
      <div className="btn-row">
        <button onClick={() => call('register')}>Register</button>
        <button onClick={() => call('login')}>Login</button>
      </div>
<<<<<<< HEAD
      <pre>{msg}</pre>
=======

      {msg && <pre>{msg}</pre>}
>>>>>>> 255326d (Final)
    </div>
  );
}

