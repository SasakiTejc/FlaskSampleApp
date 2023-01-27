from flask import Flask,render_template,request
app = Flask(__name__)

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    flg = False
    return render_template('index.html',title="form sample",message="this is jinja template sample",flg=flg)



if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')