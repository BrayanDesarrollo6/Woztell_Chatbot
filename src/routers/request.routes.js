// Objeto que almacena las rutas (ROUTER)
const { Router } = require('express');
const router = Router();
const requestController = require('../controllers/requests.controller.js')

// Ruta 1 - ChatBot
router.post('/consultworker', requestController.consultworker)

module.exports = router;