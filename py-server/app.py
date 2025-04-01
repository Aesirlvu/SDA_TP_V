from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/sumar")
def index():
    return render_template("index.html")

@app.route("/sumar", methods=['POST'])
def sumar_matrices():
    try:
        # Recibir los datos del cliente
        data = request.get_json()
        
        # Verificar que los datos necesarios están presentes
        if not all(key in data for key in ['filas', 'columnas', 'matriz1', 'matriz2']):
            return jsonify({"message": "Datos incompletos", "data": None}), 400
        
        filas = data['filas']
        columnas = data['columnas']
        matriz1 = data['matriz1']
        matriz2 = data['matriz2']
        
        if len(matriz1) != filas or len(matriz2) != filas:
            return jsonify({"message": "Las dimensiones de las matrices no coinciden", "data": None}), 400
        
        # Crear matriz para el resultado
        resultado = []
        
        # Realizar la suma de matrices
        for i in range(filas):
            fila_resultado = []
            for j in range(columnas):
                # Sumar los elementos correspondientes
                suma = matriz1[i][j] + matriz2[i][j]
                fila_resultado.append(suma)
            resultado.append(fila_resultado)
        
        # Devolver el resultado
        return jsonify({
            "message": "Matrices sumadas exitosamente",
            "data": {
                "resultado": resultado
            }
        })
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": f"Error al procesar la solicitud: {str(e)}", "data": None}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
