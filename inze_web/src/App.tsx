import React from 'react';

import Landing from './pages/Landing'

import './style/App.css'

function App() {
  return (
    <div className="content">
      <strong className="page-title">Inze app</strong>
      <span className="subtitle">Organize seus gastos de cartão de crédito através das faturas</span>
      <Landing />
    </div>
  );
}

export default App;
