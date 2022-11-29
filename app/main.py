from flask import Flask, request, make_response, redirect, render_template
from confiDB import *


app = Flask(__name__) 


@app.route('/') 
def hello_world(): 
    return render_template('public/index.html')


@app.route('/form', methods=['GET', 'POST'])
def registrarForm():
    msg =''
    if request.method == 'POST':
        nombre              = request.form['nombre']
        sexo                = request.form['sexo']
        likes               = request.form['likes']
        descripcion         = request.form['descripcion']
        print(nombre, sexo, likes, descripcion) 
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute('INSERT INTO empleados (nombre,sexo,likes,descripcion) VALUES (%s, %s, %s, %s, %s)', (nombre, sexo, likes, descripcion))
        conexion_MySQLdb.commit()
            
            
        #sql         = "INSERT INTO empleados(nombre, sexo, like, descripcion) VALUES (%s, %s, %s, %s)"
        #valores     = (nombre, sexo, like, descripcion)
        #cursor.execute(sql, valores)
        #conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro insertado")
        print("1 registro insertado, id", cursor.lastrowid)
        return render_template('public/index.html')
    else:
        msg =''
        return render_template('public/index.html', msg = 'Metodo HTTP incorrecto',)


if __name__ == '__main__': 
    app.run(debug=True, port=5000) 