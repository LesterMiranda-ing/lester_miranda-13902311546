from flask import Flask, render_template, request

app = Flask(__name__)

# index 0: Inicio
@app.route('/')
def home():
    return render_template('index.html', titulo="Página de Inicio")

# pagina 1: pasarle el parametro dinamico
@app.route('/estudiante/<nombre>')
def pagina1(nombre):
    return render_template('pagina1.html', estudiante_nombre=nombre)

# pagina 2: Tabla y listas anidadas
@app.route('/pagina2')
def pagina2():
    cursos = ["Programación Web", "Bases de Datos", "Sistemas Operativos"]
    return render_template('pagina2.html', lista_cursos=cursos)

# pagina 3: Formulario GET y POST con request.form
@app.route('/pagina3', methods=['GET', 'POST'])
def pagina3():
    mensaje = None
    datos = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        nivel = request.form.get('nivel')
        datos = {
            'nombre': nombre,
            'correo': correo,
            'nivel': nivel
        }
        mensaje = "¡Formulario procesado con éxito en Flask!"

    return render_template('pagina3.html', mensaje=mensaje, datos=datos)

# pagina 4: Figure, figcaption y elementos semánticos
@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html')

if __name__ == '__main__':
    app.run(debug=True)