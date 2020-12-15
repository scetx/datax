// entry point for importing modules
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

// returns reference to root
ReactDOM.render(
    // React.StrictMode highlights potential problems in our app by providing additional checks and warnings
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);


