# app_db.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import psycopg2
import uuid

# Cargar el string de conexion de biblioteca/.env con dotenv
from dotenv import load_dotenv
import os
from pathlib import Path
# Obtener la ruta absoluta del archivo .env
env_path = Path(".env").resolve()  # Convierte a ruta absoluta
load_dotenv(env_path)
db_conn_str = os.getenv("db_conn_str")

print(env_path)
print(db_conn_str)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///biblioteca.db"
db = SQLAlchemy(app)

# Modelo de datos
Base = db.Model
Column = db.Column
String = db.String
Integer = db.Integer
Boolean = db.Boolean
DateTime = db.DateTime
ForeignKey = db.ForeignKey
relationship = db.relationship


class UsuarioDB(Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex[:6].upper())
    nombre = Column(String)
    apellido = Column(String)
    
    prestamos = relationship("PrestamoDB", back_populates="usuario")

class MaterialDB(Base):
    __tablename__ = 'materiales'
    codigo_inventario = Column(String, primary_key=True)
    titulo = Column(String)
    tipo = Column(String)  # 'libro', 'revista', 'dvd'
    autor = Column(String, nullable=True)
    isbn = Column(String, nullable=True)
    numero_paginas = Column(Integer, nullable=True)
    fecha_publicacion = Column(String, nullable=True)
    numero_edicion = Column(String, nullable=True)
    duracion = Column(Integer, nullable=True)
    director = Column(String, nullable=True)
    disponible = Column(Boolean, default=True)
    
    prestamos = relationship("PrestamoDB", back_populates="material")

class PrestamoDB(Base):
    __tablename__ = 'prestamos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(String, ForeignKey('usuarios.id_usuario'))
    id_material = Column(String, ForeignKey('materiales.codigo_inventario'))
    fecha_prestamo = Column(DateTime, default=datetime.now)
    fecha_devolucion = Column(DateTime, default=lambda: datetime.now() + timedelta(days=14))

    usuario = relationship("UsuarioDB", back_populates="prestamos")
    material = relationship("MaterialDB", back_populates="prestamos")

# Crear las tablas (solo se ejecuta una vez)
with app.app_context():
    db.create_all()


@app.route("/nuevo_material", methods=["GET", "POST"])
def nuevo_material():
    if request.method == "POST":
        codigo_inventario = uuid.uuid4().hex
        titulo = request.form["titulo"]
        tipo = request.form["tipo"]
        autor = request.form.get("autor")
        isbn = request.form.get("isbn")
        numero_paginas = request.form.get("numero_paginas")
        fecha_publicacion = request.form.get("fecha_publicacion")
        numero_edicion = request.form.get("numero_edicion")
        duracion = request.form.get("duracion")
        director = request.form.get("director")
        disponible = True
        nuevo_material = MaterialDB(
            codigo_inventario=codigo_inventario,
            titulo=titulo,
            tipo=tipo,
            autor=autor,
            isbn=isbn,
            numero_paginas=numero_paginas,
            fecha_publicacion=fecha_publicacion,
            numero_edicion=numero_edicion,
            duracion=duracion,
            director=director,
            disponible=disponible
        )
        db.session.add(nuevo_material)
        db.session.commit()
        return redirect(url_for('listar_materiales'))
    else:
        return render_template("nuevo_material.html")

@app.route('/materiales')
def listar_materiales():
    materiales = MaterialDB.query.all()
    return render_template('materiales.html', materiales=materiales)

@app.route("/nuevo_usuario", methods=["GET", "POST"])
def nuevo_usuario():
    if request.method == "POST":
        id_usuario = uuid.uuid4().hex
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        nuevo_usuario = UsuarioDB(
            id_usuario=id_usuario,
            nombre=nombre,
            apellido=apellido,
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('listar_usuarios'))
    else:
        return render_template("nuevo_usuario.html")

@app.route('/usuarios')
def listar_usuarios():
    usuarios = UsuarioDB.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route("/nuevo_prestamo", methods=["GET", "POST"])
def nuevo_prestamo():
    if request.method == "POST":
        #id_prestamo = uuid.uuid4().hex
        usuario_id = request.form["usuario_id"]
        material_id = request.form["material_id"]
        fecha_prestamo = datetime.now()
        nuevo_prestamo = PrestamoDB(
            #id_prestamo=id_prestamo,
            id_usuario=usuario_id,
            id_material=material_id,
            fecha_prestamo=fecha_prestamo,
        )
        db.session.add(nuevo_prestamo)
        db.session.commit()
        return redirect(url_for('listar_prestamos'))
    else:
        usuarios = UsuarioDB.query.all()
        materiales = MaterialDB.query.all()
        return render_template("nuevo_prestamo.html", usuarios=usuarios, materiales=materiales)
@app.route('/prestamos')

def listar_prestamos():
    prestamos = PrestamoDB.query.all()
    return render_template('prestamos.html', prestamos=prestamos)

@app.route('/nueva_lectura')
def nueva_lectura():
    usuarios = UsuarioDB.query.all()
    usuario_seleccionado = request.args.get('usuario_id')
    materiales = []
    
    if usuario_seleccionado:
        usuario = UsuarioDB.query.get(usuario_seleccionado)
        print("Préstamos", usuario.prestamos)
        materiales = [prestamo.material for prestamo in usuario.prestamos]
    print(usuarios)
    print(materiales)
    print(usuario_seleccionado)
    return render_template('nueva_lectura.html', 
                         usuarios=usuarios,
                         materiales=materiales,
                         usuario_seleccionado=usuario_seleccionado)

@app.route('/posts')
def listar_posts():
    posts = MaterialDB.query.all()
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

