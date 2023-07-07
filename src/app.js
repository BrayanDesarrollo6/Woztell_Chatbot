// Librerias o modulos de NodeJS y su configuración
const express = require('express');
const morgan = require('morgan');
const app = express();
const cors = require('cors');
const XLSX = require('xlsx');
const fs = require('fs');

// Variables de entorno (Puerto)
app.set('port', process.env.PORT || 6000);

// Middleware
app.use(morgan('dev')); 
app.use(express.json());

// Recibir peticiones de otros puertos o host
app.use(cors());

// Routes
app.use(require('./routers/request.routes'))

module.exports = app;