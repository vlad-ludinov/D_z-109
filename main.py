from flask import Flask, render_template, request, url_for, redirect, make_response

app = Flask(__name__)
app.secret_key = b'd8e2684fc8aa988e4a87b34566787643c25460406c2285f67014f433b6cf3230'


@app.route('/hello', methods=['GET', 'POST'])
def hello():

    user = {'username': request.cookies.get('username')}

    if request.method == 'POST':
        if request.form.get('delete_button'):
            response = redirect(url_for('submit'))
            response.set_cookie('username', '', max_age=0)
            return response

    return render_template('hello.html', **user)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = redirect(url_for('hello'))
        response.set_cookie('username', name)
        return response
        # return redirect(url_for('hello'))
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
