#Archivo python con todo el desarrollo del codigo (usando Flask)
from flask import Flask, render_template, request

app = Flask(__name__)
#diccionario de productos(farmacos)
productos = [
    {'nombre': 'Aspirina', 'precio': '$5'},
    {'nombre': 'Ibuprofeno', 'precio': '$7'},
    {'nombre': 'Paracetamol', 'precio': '$4'},
    {'nombre': 'Amoxicilina', 'precio': '$10'},
    {'nombre': 'Loratadina', 'precio': '$6'}
]
#llamada a la platilla raiz
@app.route('/')
def form():
    return render_template('index.html', productos=productos)
#funcion para agregar los datos proporcionados por el usuario usando .request
@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    telefono = request.form.get('telefono')
    producto_seleccionado = next((producto for producto in productos if producto['nombre'] == request.form.get('producto')), None)
    forma_pago = request.form.get('pago')
    forma_de_envio= request.form.get('envio')
    observaciones = request.form.get('observaciones')
    if nombre and direccion and telefono and producto_seleccionado and forma_pago:
        return render_template('reporte.html', nombre=nombre, direccion=direccion, telefono=telefono, producto=producto_seleccionado, pago=forma_pago, envio=forma_de_envio, observaciones=observaciones)
    else:
        return "Por favor, completa todos los campos del formulario."

if __name__ == '__main__':
    app.run(debug=True)
