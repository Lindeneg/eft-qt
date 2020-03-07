const Plural = (len, s) => {
    if (len === 1) {
      return s
    } else {
      return s + "s"
    }
  }

  export default Plural;