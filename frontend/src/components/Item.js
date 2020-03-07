import React from 'react';
import { List } from 'antd';

import Replacer from '../Tools/Replacer';
import BCString from '../Tools/BCString';
import Plural from '../Tools/Plural';

const ItemDescription = (data) => {
  const newData = Replacer(data);
  return `
  Appears in ${newData.quests.length} ${Plural(newData.quests.length, "Quest")} | 
  Used ${newData.hideout.length} ${Plural(newData.hideout.length, "time")} in Hideout 
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
                title={<a href="/">{item.name}</a>}
                description={ItemDescription(item.notes)}
            />
            </List.Item>
        )}
        />
    );
}

export default Item;