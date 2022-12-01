from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

empleados = ['Ana','Maria','Felipe','Juan']



@app.route('/')
def hola_mundo():
    return render_template('index.html',numero_empleado = len(empleados))


@app.route('/quienes')
def quienes():
    return "SOMOS NOSOTROS"


@app.route('/usuarios/<string:nombre_user>')
def usuarios(nombre_user):
    return "Bienvenidos a la web " + nombre_user

@app.route('/post')
@app.route('/post/<int:numero>')
def post(numero=0):
    #return "NUMERO DE POST " + str(numero)
    return "NUMERO DE POST {}" .format(numero)


@app.route('/datosuser/<int:id>/<string:nombre>')
def datosuser(id,nombre):
    #return "NUMERO DE POST " + str(numero)
    return "ID: {} NOMBRE {}" .format(id,nombre)








if __name__ == "__main__":
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)