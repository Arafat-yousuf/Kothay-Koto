var sql = require("mssql");
var express = require('express');
var app = express();
// config for your database
var config = {
    user: 'sa',
    password: '123456',
    server: 'MI-AMOR\\SQLEXPRESS', 
    database: 'kothayKotoDB' ,
    encrypt: false
};

const pullTable = async () => {
    try {
        const pool = await sql.connect(config);
        const sqlQuery = 'SELECT * FROM Catalog';
        const result = await pool.request().query(sqlQuery);
        return result.recordset;
    } catch (err) {
        throw err;
    }
};

exports.pullTable = pullTable;