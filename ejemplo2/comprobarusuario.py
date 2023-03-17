from conexion import conectar

def comprobar_usuario(email, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT * FROM usuarios WHERE email = %s AND contrasena = %s"
    cursor.execute(query, (email, contrasena))

    usuario = cursor.fetchone()

    if usuario:
        # Si las credenciales son correctas, devolver los datos del usuario
        return {'id': usuario[0], 'nombre': usuario[1], 'email': usuario[2]}
    else:
        # Si las credenciales son incorrectas, devolver None
        return None
