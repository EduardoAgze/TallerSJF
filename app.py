from flask import Flask
from controller.auto_controller import index, agregar, siguiente

app = Flask(__name__)
app.secret_key = '3108' 

app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/agregar', view_func=agregar, methods=['POST'])
app.add_url_rule('/siguiente', view_func=siguiente, methods=['POST'])

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)