import React from 'react';
import axios from 'axios';

import { Card } from 'antd';

import Replacer from '../Tools/Replacer';
import BCString from '../Tools/BCString';


const mQuests = (data, type) => {
    let q = [];
    try {
        let l = data.quests.length;
        if (typeof(l) !== undefined) {
            Object.keys(data[`${type}`]).forEach(i => {
                q.push(data[`${type}`][`${i}`]);
            });
        } 
    } catch (err) {
        console.error("DetailViewError", err);
    }
    return q;
}

const Title = (d, s) => {
    
}


class ItemDetail extends React.Component {
    
    state = {
        item: {},
        img: {},
        notes: {}
    }

    componentDidMount() {
        const itemName = this.props.match.params.name;
        axios.get(`http://127.0.0.1:8000/api/${itemName}`)
        .then(res => {
            this.setState({
                item: res.data,
                img: Replacer(res.data.img_info),
                notes: Replacer(res.data.notes)
            });
        })
    }

    render() {

        const quests = [];
        const hideout = [];
       
        for (const [index, value] of mQuests(this.state.notes, "quests").entries()) {
            quests.push(<li key={index}>{value}</li>);
        }
        for (const [index, value] of mQuests(this.state.notes, "hideout").entries()) {
            hideout.push(<li key={index}>{value}</li>);
        }

        return (
            <Card title={this.state.item.name}>
                <img src={this.state.img.path} height={this.state.img.height} width={this.state.img.width} alt=""/>
                <br/><br/>
                <a href={this.state.item.url}>Tarkov Wiki</a>
                <p>{BCString(this.state.notes.barter_item, this.state.notes.crafting_item)}</p>
                <h5>{Title(quests)}</h5>
                {quests}
                <h5>{Title(hideout)}</h5>
                {hideout}
            </Card>
        );
    }
}

export default ItemDetail;