from flask import Flask, render_template

app = Flask(__name__)

app.config.update(
    DEBUG=True,
)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/collision.html')
def webDesigns():
    return render_template('collision.html')

@app.route('/mechanical.html')
def webHosting():
    return render_template('mechanical.html')

@app.route('/refining.html')
def graphicDesigns():
    return render_template('refining.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0')