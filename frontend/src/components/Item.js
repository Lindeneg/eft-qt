import React from 'react';
import { List } from 'antd';


const ItemDescription = (data) => {
  let mData = data.replace(/'/g, '"');
  mData = mData.replace(/True/g, true);
  mData = mData.replace(/False/g, false);
  const newData = JSON.parse(mData);
  return `
  Appears in ${newData.quests.length} ${Plural(newData.quests.length, "Quest")} | 
  Used ${newData.hideout.length} ${Plural(newData.hideout.length, "time")} in Hideout 
  ${UsedWhereString(newData.barter_item, newData.crafting_item)}`;
}


const UsedWhereString = (barter, crafting) => {
  if (barter === true && crafting === true) {
    return "| Barter Item | Crafting Item";
  }
  if (barter === true && crafting === false) {
    return "| Barter Item";
  }
  if (barter === false && crafting === true) {
    return "| Crafting Item";
  }
  if (barter === false && crafting === false) {
    return "";
  }
}


const Plural = (len, s) => {
  if (len === 1) {
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
                title={<a href="https://ant.design">{item.name}</a>}
                description={ItemDescription(item.notes)}
            />
            </List.Item>
        )}
        />
    );
}

export default Item;