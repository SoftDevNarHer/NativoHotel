import sqlite3

# Inicialización de la base de datos
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Crear la tabla users con la columna profile_pic
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL,
                 profile_pic TEXT)''')  # Columna para la ruta de la imagen de perfil
    conn.commit()
    conn.close()

# Añadir un nuevo usuario
def add_user(username, password, profile_pic=None):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, profile_pic) VALUES (?, ?, ?)", 
                  (username, password, profile_pic))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"User {username} already exists.")
    conn.close()

# Obtener un usuario por su nombre de usuario y contraseña
def get_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

def delete_user(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()

# Inicializar la base de datos
init_db()

#delete_user('admin')

# Ejemplos de cómo agregar usuarios
#add_user('Antonio', '1234', 'uploads/user_icon.jpg')
#add_user('admin', 'password123', 'uploads/admin_icon.jpg')
