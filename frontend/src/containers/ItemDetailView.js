import React from 'react';
import axios from 'axios';

import { Card } from 'antd';

import { Replacer, BCString } from '../tools/tools';
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


const MetaCard = (i, m, n, q, h) => {
    if (i.name === undefined) {
        return (
            <span/>
        );
    } else {
        return (
            <Card title={i.name + " - " + i.item_type}>
                <img src={m.path} height={m.height} width={m.width} alt={i.name}/>
                <br/><br/>
                <a href={i.url}>Tarkov Wiki</a>
                <br/><br/>
                <p>{BCString(n.barter_item, n.crafting_item)}</p>
                <h3>{Title(q, "Quests")}</h3>
                {q}
                <h3>{Title(h, "Hideout")}</h3>
                {h}
            </Card>
        );
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
        .catch(err => {
            console.log(err);
        });
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
            MetaCard(this.state.item, this.state.img, this.state.notes, quests, hideout)
        );
    }
}


export default ItemDetail;
