import React from 'react';
import axios from 'axios';
import Items from '../components/Item';

import DEBUG from '../debug';


class ItemList extends React.Component {
    state = {
        items: []
    }
    componentDidMount() {
        let URL = 'http://127.0.0.1:8000/api/';
        if (this.props.match.url !== '/') {
            URL += `?search=${this.props.match.params.value}`;
        }
        axios.get(URL)
        .then(res => {
            this.setState({
                items: res.data
            });
        })
        .catch(err => {
            if (DEBUG === true) {
                console.error("ItemListError", err);
            }
        });
    }
    render() {
        if (this.state.items.length === 1) {
            window.location.replace(`/${this.state.items[0].name}`)
        }
        return (
            <Items data={this.state.items}/>
        );
    }
}


export default ItemList;
