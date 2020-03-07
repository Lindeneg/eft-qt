import React from 'react';
import { List } from 'antd';

import Replacer from '../Tools/Replacer';
import BCString from '../Tools/BCString';
import Plural from '../Tools/Plural';

const ItemDescription = (data) => {
  const newData = Replacer(data);
  let ql = Object.keys(newData.quests).length;
  let hl = Object.keys(newData.hideout).length;
  return `
  Appears in ${ql} ${Plural(ql, "Quest")} | 
  Used ${hl} ${Plural(hl, "time")} in Hideout 
  ${BCString(newData.barter_item, newData.crafting_item)}`;
}

const Item = (props) => {
    return (
        <List
        itemLayout="horizontal"
        dataSource={props.data}
        renderItem={item => (
            <List.Item>
            <List.Item.Meta
                title={<a href={'/' + item.name}>{item.name}</a>}
                description={ItemDescription(item.notes)}
            />
            </List.Item>
        )}
        />
    );
}

export default Item;