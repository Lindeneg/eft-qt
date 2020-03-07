import React from 'react';
import 'antd/dist/antd.css';

import DefaultLayout from './containers/Layout';
import ItemList from './containers/ItemListView';


function App() {
  return (
    <div className="App">
      <DefaultLayout>
        <ItemList />
      </DefaultLayout>
    </div>
  );
}


export default App;
