from flask import Flask, render_template, request
from conexion import conectar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    conexion = conectar()
    cursor = conexion.cursor()

    email = request.form['email']
    contrasena = request.form['contrasena']

    query = "SELECT * FROM usuarios WHERE email = %s AND contrasena = %s"
    cursor.execute(query, (email, contrasena))

    usuario = cursor.fetchone()

    if usuario:
        # Si las credenciales son correctas, redirigir a la página de inicio del usuario
        return render_template('registro.html', nombre=usuario[1])
    else:
        # Si las credenciales son incorrectas, volver a la página de login con un mensaje de error
        mensaje_error = "Credenciales incorrectas, por favor inténtelo de nuevo."
        return render_template('login.html', mensaje_error=mensaje_error)

# crear usuarios 

@app.route('/insertar', methods=['POST'])
def insertar():
    nombre = request.form['nombre']
    email = request.form['email']
    contrasena = request.form['contrasena']
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO usuarios (nombre, email, contrasena) VALUES (%s, %s, %s)"
    values = (nombre, email, contrasena)
    cursor.execute(query, values)
    conexion.commit()
    cursor.close()
    conexion.close()
    return render_template('registro.html', mensaje="El usuario ha sido insertado correctamente.")

# Función para listar los usuarios de la base de datos
@app.route('/listar', methods=['GET'])
def listar_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        for fila in usuarios:
            print(fila)
    except Exception as e:
        print(e)  # Agregar esta línea para imprimir cualquier error
        usuarios = []
    conexion.close()
    return render_template('registro.html', usuarios=usuarios)




# Ruta para eliminar usuario
@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    id_a_eliminar = request.form["id_a_eliminar"]
    conn = conectar()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM usuarios WHERE id = {id_a_eliminar}")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('registro.html', mensaje="El usuario ha sido eliminado correctamente.")

#actualizar 
@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    id_usuario = request.form["id"]
    nombre = request.form["nombre"]
    email = request.form["email"]
    contrasena = request.form["contrasena"]
    conn = conectar()
    cur = conn.cursor()
    cur.execute(f"UPDATE usuarios SET nombre='{nombre}', email='{email}',contrasena='{contrasena}' WHERE id={id_usuario}")
    conn.commit()
    cur.close()
    conn.close()
    return render_template('registro.html', mensaje="El usuario ha sido actualizado correctamente.")


if __name__ == '__main__':
    app.run(debug=True)
