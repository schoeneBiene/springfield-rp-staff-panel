from flask import Flask

app = Flask(__name__)

@app.route('/')
def routed():
    return "Hello!"


if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()