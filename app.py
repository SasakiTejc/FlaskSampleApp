from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('Index.html',title="Index with jinja",message="Jinjaテンプレート例")

@app.route('/<id>/<password>')
def index2(id,password):
    msg = 'id: %s, password: %s' %(id,password)
    return render_template('index.html',title="index whis jinja",message=msg)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')