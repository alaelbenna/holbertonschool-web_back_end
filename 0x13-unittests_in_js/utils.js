const Utils = {
  calculateNumber(type, a, b) {
    const numOne = Number(a);
    const numTwo = Number(b);

    if (type === 'SUM') {
      return (Math.round(numOne) + Math.round(numTwo));
    }
    if (type === 'SUBTRACT') {
      return (Math.round(numOne) - Math.round(numTwo));
    }
    if (type === 'DIVIDE') {
      if (Math.round(numTwo) === 0) {
        return ('Error');
      }
      return (Math.round(numOne) / Math.round(numTwo));
    } else throw (TypeError);
  }
};

module.exports = Utils;
