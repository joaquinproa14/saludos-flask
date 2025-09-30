from flask import Flask
app = Flask(__name__)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola, {nombre}! Bienvenido a mi app Flask."

if __name__ == '__main__':
    app.run(debug=True)
