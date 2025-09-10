from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<nome>')
def nome(nome):
    return  render_template('ex_3-1.html', nome = nome)


if __name__ == '__main__':
    app.run(debug=True)