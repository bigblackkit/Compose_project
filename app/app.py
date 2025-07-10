from flask import Flask
import platform
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def info():
    return f"""
    <html>
    <body>
    <h2>Системная информация:</h2>
    <ul>
        <li><b>Текущая дата:</b> {datetime.now().strftime('%Y-%m-%d')}</li>
        <li><b>Время:</b> {datetime.now().strftime('%H:%M:%S')}</li>
        <li><b>Версия Python:</b> {platform.python_version()}</li>
        <li><b>Имя хоста:</b> {socket.gethostname()}</li>
        <li><b>IP адрес:</b> {socket.gethostbyname(socket.gethostname())}</li>
    </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
