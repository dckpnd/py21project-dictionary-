from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mainpage.html')


@app.route("/begins", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for('user', usr=user))
    else:
        return render_template('begins.html')


@app.route("/<usr>")
def user(usr):
    return f'<h1> Ваше слово {usr} <h1>'


if __name__ == '__main__':
    app.run(debug=True)