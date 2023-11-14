#Por: Luis Armijos

from flask import Flask, render_template
from flask_socketio import SocketIO, send 
#Send permite enviar un mensaje desde el servidor

#Instanciar flask
app = Flask(__name__)

#Instanciar SocketIO
app.config['SECRET_KEY']='secret'

#Guardar conexión
socketio = SocketIO(app)

# Definir una función 
@app.route('/app')
def index():
    #return 'Hola desde flask'
    return render_template('index.html')

#Utilizar el socketio
@socketio.on('message')
def send_message(msg):
    print('Mensaje: ' + msg)

#Ejecutar el servidor 
if __name__ == "__main__":
    app.run()