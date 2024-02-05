# create flask app 
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():

    a = 10
    return f'Hello, World!{a}'

if __name__ == '__main__':
    app.run(debug=True)