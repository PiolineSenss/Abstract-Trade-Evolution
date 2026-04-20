from flask import Flask, send_from_directory
from flask_cors import CORS
from routers.auth import auth_bp   # импортируем Blueprint

app = Flask(__name__, static_folder='static')
CORS(app)

# Регистрируем Blueprint для авторизации
app.register_blueprint(auth_bp)

# Отдаём index.html из папки static
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)