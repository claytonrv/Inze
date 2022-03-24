import React from 'react';

import { useTranslation } from 'react-i18next';

import Landing from './pages/Landing'
import Translations from './components/Translations';

import './style/App.css'

function App() {
  const { t } = useTranslation();
  return (
    <div className="content">
      <strong className="page-title">{t('app.header')}</strong>
      <span className="subtitle">{t('app.subtitle')}</span>
      <Landing />
      <Translations />
    </div>
  );
}

export default App;
