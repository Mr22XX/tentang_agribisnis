from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
comments = []

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Username atau Password Salah')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        if name and comment:
            comments.append((name, comment))
    return render_template('download.html', comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
