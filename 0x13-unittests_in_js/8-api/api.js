const express = require('express');

const app = express();
const connection = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.listen(connection, () => {
  console.log(`API available on localhost port ${connection}`);
});

module.exports = app;
