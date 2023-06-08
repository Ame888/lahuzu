from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/jieshao.html")
def jieshao():
    return render_template('jieshao.html')

@app.route("/qushi.html")
def qushi():
    return render_template('qushi.html')

@app.route("/ciyun.html")
def ciyun():
    return render_template('ciyun.html')

@app.route("/qinggan.html")
def qinggan():
    return render_template('qinggan.html')

@app.route("/zhuti.html")
def zhuti():
    return render_template('zhuti.html')





if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='2000')

