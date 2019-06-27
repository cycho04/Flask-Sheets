from flask import Flask, render_template, request, flash, Response, redirect, url_for
from forms import NewEmployeeForm
from sheets import MakeEmployee
from secret import secret_key


app = Flask(__name__)
app.secret_key = secret_key


@app.route('/new', methods=['GET', 'POST'])
def new():
    form = NewEmployeeForm()
    if request.method == 'POST':
        first = request.form.get('first')
        last = request.form.get('last')
        casino = request.form.get('casino')
        title = request.form.get('title')
        hired = request.form.get('hired')
        EIN = request.form.get('EIN')
        MakeEmployee(first, last, casino, title, hired, EIN)
        if form.validate() == False:
            flash('Please fill out the marked sections')
            return render_template('home.html', form=form)
        elif form.validate_on_submit():

            return redirect(url_for('new'))
    elif request.method == 'GET':
        return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
