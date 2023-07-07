// Almacenar objeto de funciones de enrutamiento - pertenece a router
const requestsController = {}
const { log } = require('console');
const { json } = require('express');
// Variables compartidas
const fs = require('fs');
const spawn = require("child_process").spawn;
const utf8 = require('utf8');
// Variables Reporte Nomina, LQ y ReLQ
const XLSX = require('xlsx');

// Directories Plantillas
PythonConsultWorker = "./src/python/ConsultarColaborador.py";

// Funcion descargar plantilla Excel
requestsController.consultworker = (req, res) => {
    const { body } = req;
    console.log(body);
    //const jsonString = JSON.stringify(body);
    //console.log(jsonString);
    res.json({ message:'Solicitud recibida correctamente, sin registro'});
    // if(jsonString != "")
    // {
    //     const process = spawn('python',[PythonPlantillasHorizontal,jsonString]);
    //     process.stderr.on("data",(data)=>{
    //         console.error('stderr:',data.toString());
    //     })
    //     process.stdout.on('data', (data) => {
    //         Respuesta = data.toString();
    //         Respuesta = Respuesta.split("\r\n").join("");
    //         Respuesta = Respuesta.split("\n").join("");
    //         console.log(Respuesta);
    //         if(Respuesta == "No existe registro"){
    //             res.json({ message:'Solicitud recibida correctamente, sin registro'});
    //         }
    //         else{
    //             process.stdout.on('end', function(data) {
    //                 res.json({ message:'Solicitud recibida correctamente'});
    //             })
    //         }
    //     });
    // }
}

// Exportar módulo
module.exports = requestsController;