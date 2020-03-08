import React from 'react';
import { List } from 'antd';

import { Replacer, BCString } from '../Tools/Tools';
import DEBUG from '../debug';

const ItemDescription = (d) => {
  const newData = Replacer(d);
  try {
      let ql = Object.keys(newData.quests).length;
      let hl = Object.keys(newData.hideout).length;
      return `
      Appears in ${ql} ${Plural(ql, "Quest")} | 
      Used ${hl} ${Plural(hl, "time")} in Hideout 
      ${BCString(newData.barter_item, newData.crafting_item)}
      `;
  } catch (err) {
      if (DEBUG === true) {
          console.error("ItemError", err);
      }
      return "";
  }
}

const Plural = (l, s) => {
    if (l === 1) {
      return s
    } else {
      return s + "s"
    }
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
