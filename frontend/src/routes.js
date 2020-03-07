import React from 'react';
import { Route } from 'react-router-dom';

import ItemList from './containers/ItemListView';

const DefaultRouter = () => (
    <div>
        <Route exact path='/' component={ItemList} />
        <Route exact path='/:name' component={ItemList} />
    </div>
);

export default DefaultRouter;