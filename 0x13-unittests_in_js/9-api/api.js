const express = require('express');

const app = express();
const connection = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.listen(connection, () => {
  console.log(`API available on localhost port ${connection}`);
});

app.get('/cart/:id', function(req, res) {
  const id = req.params.id;
  if (!(isNaN(Number(id)))) {
    res.send(`Payment methods for cart ${id}`);
  }
  res.sendStatus(404).end();
});

module.exports = app;
