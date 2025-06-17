from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import bcrypt


app = Flask(__name__)

# Configuración de la base de datos (ajusta esto según tu configuración de MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/registrosApi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contraseña = db.Column(db.String(60), nullable=False)

# Ruta de registro
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    nombre_usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    # Verificar si el usuario ya existe en la base de datos
    usuario_existente = Usuario.query.filter_by(usuario=nombre_usuario).first()
    if usuario_existente:
        return jsonify({"mensaje": "El usuario ya existe"}), 400

    # Hash de la contraseña antes de almacenarla en la base de datos
    hashed_contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

    # Crear un nuevo usuario
    nuevo_usuario = Usuario(usuario=nombre_usuario, contraseña=hashed_contraseña)

    # Agregar el nuevo usuario a la base de datos
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Registro exitoso"}), 201

# Ruta de inicio de sesión
@app.route('/inicio-sesion', methods=['POST'])
def inicio_sesion():
    data = request.get_json()
    nombre_usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    # Buscar al usuario en la base de datos
    usuario = Usuario.query.filter_by(usuario=nombre_usuario).first()

    if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario.contraseña.encode('utf-8')):
        return jsonify({"mensaje": "Inicio de sesión exitoso"}), 200
    else:
        return jsonify({"mensaje": "Error de autenticación"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)
