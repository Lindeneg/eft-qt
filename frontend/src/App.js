import React from 'react';
import { BrowserRouter } from 'react-router-dom';

import DefaultRouter from './routes';
import DefaultLayout from './containers/Layout';

import 'antd/dist/antd.css';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <DefaultLayout>
          <DefaultRouter />
        </DefaultLayout>
      </BrowserRouter>
    </div>
  );
}

export default App;
