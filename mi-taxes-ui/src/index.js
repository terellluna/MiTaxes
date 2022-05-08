import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter, Route, Routes, Navigate } from 'react-router-dom';
import About from './components/About';
import CalculateTaxes from './components/CalculateTaxes';
import Donate from './components/Donate'

ReactDOM.render(
  <BrowserRouter>
    <Routes>
      <Route exact path="" element={<App />}>
        {/* <Navigate replace to="/about"/> */}
        <Route exact path="/calculate-taxes" element = {<CalculateTaxes/>}/>
        <Route exact path="/about" element = {<About/>}/>
        <Route exact path="/donate" element = {<Donate/>}/>
      </Route>
    </Routes>
  </BrowserRouter>,
  document.getElementById('root')
);
