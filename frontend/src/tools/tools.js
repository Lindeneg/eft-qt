import DEBUG from '../debug';


const BCString = (barter, crafting) => {
    let bcstring = "";
    try {
      if (barter === true && crafting === true) {
        bcstring = "| Barter Item | Crafting Item";
    }
      if (barter === true && crafting === false) {
        bcstring = "| Barter Item";
    }
      if (barter === false && crafting === true) {
        bcstring = "| Crafting Item";
    }
    } catch (err) {
      if (DEBUG === true) {
        console.error("BCString", err);
      }
    } finally {
        return bcstring;
    }
}


const Replacer = (data) => {
    let mData = data.replace(/'/g, '"');
    mData = mData.replace(/True/g, true);
    mData = mData.replace(/False/g, false);
    try {
        mData = JSON.parse(mData);
    } catch (err) {
        if (DEBUG === true) {
          console.error("ReplacerError", err, mData);
        }
        mData = data;
    } finally {
        return mData;
    }
}


export { BCString, Replacer };
