import express from 'express'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

const port = 3000
const url = 'localhost'

const app = express()

app.use(express.json())

app.use(express.static(path.join(__dirname, 'public')))

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public/index.html'))
})

app.post("/", (req, res) =>{
    try {
        const {filas, columnas, matriz1, matriz2} = req.body
        let resultado = [];

        if (typeof filas !== 'number' || typeof columnas !== 'number') {
            return res.status(400).json({message: "Las filas y columnas deben ser números"});
        }
        
        for (let i = 0; i < filas; i++) {
            resultado.push([]);
            for (let j = 0; j < columnas; j++) {
                resultado[i].push(matriz1[i][j] + matriz2[i][j]);
            }
        }

        res.json({message: "Matrices sumadas!", data: {resultado}})
    } catch(error){
        console.error("Error:", error);
        res.status(500).json({message: "Hubo un error procesando la solicitud"})
    }
})

app.listen(port, () => {
  console.log(`Server running at http://${url}:${port}`)
})