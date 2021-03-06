import React from 'react';
import { Route } from 'react-router-dom';

import ItemList from './containers/ItemListView';
import ItemDetail from './containers/ItemDetailView';

const DefaultRouter = () => (
    <div>
        <Route exact path='/' component={ItemList} />
        <Route exact path='/:name' component={ItemDetail} />
        <Route exact path='/search/:value' component={ItemList} />
    </div>
);

export default DefaultRouter;
