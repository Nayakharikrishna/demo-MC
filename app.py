
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Flask Application</title>
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h1>Welcome to My DevOps Project!</h1>
        <p>Flask application deployed using Docker and Jenkins.</p>

        <button onclick="alert('Goodbye!')">Left</button>
        <button onclick="alert('Welcome!')">Click Here</button>
        <button onclick="alert('Why do programmers prefer dark mode? Because light attracts bugs!')">Right</button>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

