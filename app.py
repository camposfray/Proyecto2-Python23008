from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/paquetel')
def paquetel():
    return render_template('sitio/paquetel.html')


@app.route('/paquetel/<seccion>')
def paquetel_seccion():
    return render_template('sitio/paquetel.html', seccion='local1')


@app.route('/paqueter')
def paqueter():
    return render_template('sitio/paqueter.html')

@app.route('/paquetei')
def paquetei():
    return render_template('sitio/paquetei.html')

@app.route('/carrito')
def carrito():
    return render_template('sitio/carrito.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')





if __name__ == '__main__':
    app.run(debug=True)