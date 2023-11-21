from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def eje1():
    promedio = None
    estado = None
    mostrarResultado = False

    if request.method == 'POST':
        notas = [
            float(request.form['nota1']),
            float(request.form['nota2']),
            float(request.form['nota3'])
        ]
        asistencia = float(request.form['asistencia'])
        for nota in notas:
            if nota < 10 or nota > 70:
                break
        else:
            promedio = round(sum(notas) / len(notas), 2)
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"

    mostrarResultado = True
    return render_template('ejercicio1.html', estado=estado, promedio=promedio, mostrarResultado=mostrarResultado )

@app.route('/ejercicio2', methods=['GET', 'POST'])
def eje2():
    nombreLargo = ""
    longitudLargo = ""
    if request.method == 'POST':
        nombres = [
            request.form['nombre1'],
            request.form['nombre2'],
            request.form['nombre3']
        ]
        nombreLargo = max(nombres, key=len)
        longitudLargo = len(nombreLargo)
    return render_template('ejercicio2.html', nombreLargo=nombreLargo, longitudLargo=longitudLargo)

if __name__ == '__main__':
    app.run(debug=True)