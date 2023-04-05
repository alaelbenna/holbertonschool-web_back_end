module.exports = function calculateNumber(a, b) {
  const numOne = Number(a);
  const numTwo = Number(b);

  return (Math.round(numOne) + Math.round(numTwo));
};
