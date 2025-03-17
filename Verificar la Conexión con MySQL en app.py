from flask import Flask
from conexion.conexion import obtener_conexion

app = Flask(__name__)

@app.route('/test_db')
def test_db():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return str(resultados)
    except Exception as e:
        return f"Error de conexión: {e}"

if __name__ == '__main__':
    app.run(debug=True)
