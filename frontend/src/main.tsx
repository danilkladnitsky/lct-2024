import React from 'react'
import ReactDOM from 'react-dom/client'
import {configure} from '@gravity-ui/uikit';

import App from './App.tsx'

configure({
  lang: 'ru',
});

import '@gravity-ui/uikit/styles/fonts.css';
import '@gravity-ui/uikit/styles/styles.css';
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
