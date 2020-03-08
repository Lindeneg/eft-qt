import React from 'react';
import axios from 'axios';

import { Card } from 'antd';

import { Replacer, BCString } from '../Tools/Tools';
import DEBUG from '../debug';


const mQuests = (d, t) => {
    let q = [];
    try {
        let l = d.quests.length;
        if (typeof(l) !== undefined) {
            Object.keys(d[`${t}`]).forEach(i => {
                q.push(d[`${t}`][`${i}`]);
            });
        } 
    } catch (err) {
        if (DEBUG === true) {
            console.error("ViewError", err);
        }
    }
    return q;
}

const Title = (d, s) => {
    if (d.length > 0) {
        return s;
    } else {
        return "";
    }
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
        
        try {
            for (const [index, value] of mQuests(this.state.notes, "quests").entries()) {
                quests.push(<li key={index}>{value}</li>);   
            }
        } catch (err) {
            if (DEBUG === true) {
                console.error("ViewError", err);
            }
        }

        try {
            for (const [index, value] of mQuests(this.state.notes, "hideout").entries()) {
                hideout.push(<li key={index}>{value}</li>);
            }
        } catch (err) {
            if (DEBUG === true) {
                console.error("ViewError", err);
            }
        }

        return (
            <Card title={this.state.item.name + " - " + this.state.item.item_type}>
                <img src={this.state.img.path} height={this.state.img.height} width={this.state.img.width} alt={this.state.item.name}/>
                <br/><br/>
                <a href={this.state.item.url}>Tarkov Wiki</a>
                <br/><br/>
                <p>{BCString(this.state.notes.barter_item, this.state.notes.crafting_item)}</p>
                <h3>{Title(quests, "Quests")}</h3>
                {quests}
                <h3>{Title(hideout, "Hideout")}</h3>
                {hideout}
            </Card>
        );
    }
}

export default ItemDetail;