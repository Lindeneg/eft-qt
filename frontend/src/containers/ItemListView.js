import React from 'react';
import axios from 'axios';
import Items from '../components/Item';


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
    }

    render() {
        return (
            <Items data={this.state.items}/>
        );
    }
}

export default ItemList;