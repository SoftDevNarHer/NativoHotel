from flask import Flask, render_template, request, redirect, url_for, flash, session
import db  

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'xdxdxd'  

db.init_db()

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('index'))  
    return redirect(url_for('login'))  

@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', 
                               username=session['username'],
                               profile_pic=session.get('profile_pic'))  # Añadir profile_pic al contexto
    else:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.get_user(username, password) 

        if user:
            session['username'] = username
            session['profile_pic'] = user[3]  # El cuarto campo será profile_pic
            flash('Sesión iniciada correctamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciales incorrectas!', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('profile_pic', None)  # También eliminar la imagen de perfil de la sesión
    flash('Has cerrado sesión correctamente!', 'info')
    return redirect(url_for('login'))   

@app.route('/reservacion')
def reservacion():
    if 'username' in session:
        return render_template('reservacion.html', username=session['username'])
    else:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))

@app.route('/queja')
def queja():
    if 'username' in session:
        return render_template('queja.html', username=session['username'])
    else:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))

@app.route('/mantenimiento')
def mantenimiento():
    if 'username' in session:
        return render_template('mantenimiento.html', username=session['username'])
    else:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))

@app.route('/clientes')
def clientes():
    if 'username' in session:
        return render_template('clientes.html', username=session['username'])
    else:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))
    
@app.route('/disponibilidad', methods=['GET', 'POST'])
def disponibilidad():
    if request.method == 'POST':
        # Aquí puedes manejar la lógica de disponibilidad si es necesario
        return redirect(url_for('reservation_options'))
    return render_template('disponibilidad.html')

@app.route('/opciones_reserva')
def reservation_options():
    return render_template('reservation_option.html')


if __name__ == '__main__':
    app.run(debug=True)
