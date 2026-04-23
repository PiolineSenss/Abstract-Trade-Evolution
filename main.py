# -*- coding: utf-8 -*-
from flask import Flask, render_template, make_response
from flask_cors import CORS
from routers.auth import auth_bp

app = Flask(__name__, static_folder='static')
CORS(app)

app.config['JSON_AS_ASCII'] = False       # чтобы русский в JSON не убегал
app.jinja_env.encoding = 'utf-8'          # принудительно для шаблонов

app.register_blueprint(auth_bp)

@app.route('/')
def serve_index():
    resp = make_response(render_template('index.html'))
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)