let pullTable = require('./pullTable.js');
var express = require('express');
var app = express();

app.get('/', async (req, res, next) => {
  try {
    res.set('Access-Control-Allow-Origin', '*');
    const result = await pullTable.pullTable();
    return res.status(200).json(result);
  } catch (error) {
    next(error);
  }
});

app.listen(5000, () => {console.log('Server is running..')});