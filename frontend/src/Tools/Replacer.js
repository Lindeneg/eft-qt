const Replacer = (data) => {
    let mData = data.replace(/'/g, '"');
    mData = mData.replace(/True/g, true);
    mData = mData.replace(/False/g, false);
    const itemData = JSON.parse(mData);
    return itemData;
  }


  export default Replacer;