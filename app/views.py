from app import app
from flask import render_template, request
from .forms import IDForm


@app.route('/')
@app.route('/index')
def index():
    form = IDForm()
    return render_template('index.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        return render_template('results.html')
