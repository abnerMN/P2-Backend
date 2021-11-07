from flask import Flask, jsonify, request
from flask_cors import CORS
from usuario import Usuario
from publicacion import Publicacion
from datetime import datetime

Usuarios = []
Publicaciones = []
contadorPublicaciones = 100
Usuarios.append(Usuario("Darwin", "Arevalo", "M",
                "admin", "admin@ipc1.com", "admin@ipc1"))
app = Flask(__name__)
CORS(app)


def numero(passwoord):
    numero = False
    for i in passwoord:
        if i.isdigit():
            numero = True
            break
    return numero


def simbolo(passwoord):
    caracter = False
    for i in passwoord:
        if i.isalpha() == False and numero(i) == False:
            caracter = True
            break
    return caracter

# funcion para obtener todos los usuarios


@app.route('/usuarios', methods=['GET'])
def usuarios():
    global Usuarios
    Datos = []
    for u in Usuarios:
        dato = {
            "nombre": u.getNombre(),
            "apellido": u.getApellido(),
            "genero": u.getGenero(),
            "username": u.getUsername(),
            "correo": u.getEmail(),
            "password": u.getPassword()
        }
        Datos.append(dato)
    respuesta = jsonify(Datos)
    return (respuesta)

# funcion para agregar usuarios


@app.route('/agregarUsuario', methods=['POST'])
def AgregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    genero = request.json['genero']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    bandera_correo = False
    bandera_usuario = False

    for u in Usuarios:
        if u.getEmail() == email:
            bandera_correo = True
            break

    for u in Usuarios:
        if u.getUsername() == username:
            bandera_usuario = True
            break
    if bandera_correo:
        return jsonify({
            'message': '015',
            'reason': 'Correo ya existente'
            })
    else:
        if bandera_usuario:
            return jsonify({
                'message': '020',
                'reason': 'Usuario ya existente'
                })
        else:
            if len(password) >= 8:
                if numero(password):
                    if simbolo(password):
                        nuevo = Usuario(nombre, apellido, genero,
                                        username, email, password)
                        Usuarios.append(nuevo)
                        return jsonify({
                            'message': '025',
                            'reason': 'Credenciales Correctas'
                            })
                    else:
                        return jsonify({
                            'message': '021',
                            'reason': 'el password tiene que tener como minimo 1 simbolo'
                        })
                else:
                    return jsonify({
                        'message': '022',
                        'reason': 'el password tiene que tener como minimo 1 numero'
                    })
            else:
                return jsonify({
                    'message': '023',
                    'reason': 'el password tiene que tener como minimo 8 caracteres'
                })

# FUncion para realizar el login


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    bandera = False
    for u in Usuarios:
        if u.getUsername() == username:
            bandera = True
            break
    if bandera:
        for u in Usuarios:
            if u.getUsername() == username:
                if u.getPassword() == password:
                    return jsonify({
                        'message': '200',
                        'reason': 'Credenciales Correctas'
                        })
                else:
                    return jsonify({
                        'message': '010',
                        'reason': 'contraseña incorrecta'
                        })
    else:
        return jsonify({
            'message': '005',
            'reason': 'Usuario no registrado'
            })

# funcion para buscar un usuario


@app.route('/buscar/<string:username>', methods=['GET'])
def buscar(username):
    global Usuarios
    Datos = []
    respuesta = jsonify(Datos)
    bandera = False
    for u in Usuarios:
        if u.getUsername() == username:
            dato = {
                "nombre": u.getNombre(),
                "apellido": u.getApellido(),
                "genero": u.getGenero(),
                "username": u.getUsername(),
                "correo": u.getEmail(),
                "password": u.getPassword()
                }
            Datos.append(dato)
            respuesta = jsonify(Datos)
            bandera = True
            break
    if bandera:
        return respuesta
    else:
        return jsonify({
            'message': '026',
            'reason': 'Usuario no registrado'
            })

# funcion para modificar un usuario


@app.route('/modificar/<string:username>', methods=['PUT'])
def modificarUsuario(username):
    global Usuarios
    bandera = False
    for u in Usuarios:
        if u.getUsername() == username:
            password = request.json['password']
            if len(password) >= 8:
                if numero(password):
                    if simbolo(password):
                        u.setNombre(request.json['nombre']),
                        u.setApellido(request.json['apellido']),
                        u.setGenero(request.json['genero']),
                        u.setUsername(request.json['username']),
                        u.setEmail(request.json['email']),
                        u.setPassword(password)
                        bandera = True
                        break
                    else:
                        return jsonify({
                            'message': '021',
                            'reason': 'el password tiene que tener como minimo 1 simbolo'
                        })
                else:
                    return jsonify({
                        'message': '022',
                        'reason': 'el password tiene que tener como minimo 1 numero'
                    })
            else:
                return jsonify({
                    'message': '023',
                    'reason': 'el password tiene que tener como minimo 8 caracteres'
                })

    if bandera:
        return jsonify({
            'message': '030',
            'reason': 'Se ha actualizado los datos exitosamente'
            })
    else:
        return jsonify({
            'message': '031',
            'reason': 'No se pudo Actualizar los datos'
            })

# Funcion para eliminar un usuario


@app.route('/eliminar/<string:username>', methods=['DELETE'])
def eliminarUsuario(username):
    global Usuarios
    bandera = False
    for i in range(len(Usuarios)):
        if Usuarios[i].getUsername() == username:
            del Usuarios[i]
            bandera = True
            break
    if bandera:
        return jsonify({
            'message': '050',
            'reason': 'Se eliminó el usuario exitosamente'
            })
    else:
        return jsonify({
            'message': '049',
            'reason': 'Error al eliminar el usuario'
            })

# funcion para agregar varios usuarios


@app.route('/cargaUsuarios', methods=['POST'])
def cargaUsuarios():
    global Usuarios
    arg = request.json['name'].split()
    if (len(arg) == 2):
        nombre = arg[0]
        apellido = arg[1]
    else:
        nombre = arg[0]
        apellido = ""

    genero = request.json['gender']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    bandera_correo = False
    bandera_usuario = False
    for u in Usuarios:
        if u.getEmail() == email:
            bandera_correo = True
            break

    for u in Usuarios:
        if u.getUsername() == username:
            bandera_usuario = True
            break
    if bandera_correo:
        return jsonify({
            'message': '015',
            'reason': 'Correo ya existente'
            })
    else:
        if bandera_usuario:
            return jsonify({
                'message': '020',
                'reason': 'Usuario ya existente'
                })
        else:
            if len(password) >= 8:
                if numero(password):
                    if simbolo(password):
                        nuevo = Usuario(nombre, apellido, genero,
                                        username, email, password)
                        Usuarios.append(nuevo)
                        return jsonify({
                            'message': '025',
                            'reason': 'Credenciales Correctas'
                            })
                    else:
                        return jsonify({
                            'message': '021',
                            'reason': 'el password tiene que tener como minimo 1 simbolo'
                        })
                else:
                    return jsonify({
                        'message': '022',
                        'reason': 'el password tiene que tener como minimo 1 numero'
                    })
            else:
                return jsonify({
                    'message': '023',
                    'reason': 'el password tiene que tener como minimo 8 caracteres'
                })


# funcion para agregar usuarios
@app.route('/imgPublicaciones', methods=['POST'])
def agregarPublicaciones():
    global Publicaciones
    global contadorPublicaciones
    tipo = "image"
    categoria = request.json['category']
    author = request.json['author']
    url = request.json['url']
    date = request.json['date']
    bandera_usuario = False

    for u in Usuarios:
        if u.getUsername() == author:
            bandera_usuario = True
            break
    if bandera_usuario:

        nuevo = Publicacion(contadorPublicaciones, tipo,
                            categoria, author, url, date)
        contadorPublicaciones = contadorPublicaciones+1
        Publicaciones.append(nuevo)
        return jsonify({
            'message': '060',
            'reason': 'Publicacion Guardada'
        })
    else:
        return jsonify({
            'message': '061',
            'reason': 'Error al subir la publicacion Author no registrado'
        })

# funcion para agregar publicaciones videos


@app.route('/vidPublicaciones', methods=['POST'])
def agregarVPublicaciones():
    global Publicaciones
    global contadorPublicaciones
    tipo = "videos"
    categoria = request.json['category']
    author = request.json['author']
    urlTemp = request.json['url']
    arg = urlTemp.split(sep='/')
    url = arg[0]+'//www.youtube.com'+'/embed/'+arg[3]
    print(url)
    date = request.json['date']
    bandera_usuario = False

    for u in Usuarios:
        if u.getUsername() == author:
            bandera_usuario = True
            break
    if bandera_usuario:
        nuevo = Publicacion(contadorPublicaciones, tipo,
                            categoria, author, url, date)
        contadorPublicaciones = contadorPublicaciones+1
        Publicaciones.append(nuevo)
        return jsonify({
            'message': '060',
            'reason': 'Publicacion Guardada'
        })
    else:
        return jsonify({
            'message': '061',
            'reason': 'Error al subir la publicacion Author no registrado'
        })

# funcion para obtener todas las publicaciones


@app.route('/publicaciones', methods=['GET'])
def publicaciones():
    global Publicaciones
    Datos = []
    for u in Publicaciones:
        dato = {
            "id": u.getId(),
            "tipo": u.getTipo(),
            "categoria": u.getCategoria(),
            "author": u.getAuthor(),
            "date": u.getDate(),
            "url": u.getUrl()
        }
        Datos.append(dato)
    respuesta = jsonify(Datos)
    return (respuesta)

# Funcion para eliminar una publicacion


@app.route('/eliminarPb/<int:id>', methods=['DELETE'])
def eliminarPublicacion(id):
    global Publicaciones
    bandera = False
    for i in range(len(Publicaciones)):
        if Publicaciones[i].getId() == id:
            del Publicaciones[i]
            bandera = True
            break
    if bandera:
        return jsonify({
            'message': '062',
            'reason': 'Se eliminó la publicacion exitosamente'
            })
    else:
        return jsonify({
            'message': '063',
            'reason': 'Error al eliminar la publicacion'
            })

#publicacion nueva individual
@app.route('/publicarNew', methods=['POST'])
def nuevaPublicacion():
    global Publicaciones
    global contadorPublicaciones
    tipo = request.json['tipo']
    categoria = request.json['categoria']
    author = request.json['author']
    urlTemp = request.json['url']
    if (tipo=="image"):
        url = urlTemp
        date = datetime.today().strftime('%d/%m/%Y')
        nuevo = Publicacion(contadorPublicaciones, tipo,categoria, author, url, date)
        contadorPublicaciones=contadorPublicaciones+1
        Publicaciones.append(nuevo)
        return jsonify({
            'message':'060',
            'reason':'Publicacion Guardada'
        })
    else:
        arg = urlTemp.split(sep='/')
        url = arg[0]+'//www.youtube.com'+'/embed/'+arg[3]
        date = datetime.today().strftime('%d/%m/%Y')
        nuevo = Publicacion(contadorPublicaciones, tipo,categoria, author, url, date)
        contadorPublicaciones=contadorPublicaciones+1
        Publicaciones.append(nuevo)
        return jsonify({
            'message':'060',
            'reason':'Publicacion Guardada'
        })


if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=4000)
