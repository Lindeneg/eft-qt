const BCString = (barter, crafting) => {
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

  export default BCString;