from app import app
from flask import render_template, request
from .forms import IDForm
from app import models


@app.route('/')
@app.route('/index')
def index():
    form = IDForm()
    return render_template('index.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    # TODO: Отдавать только имеющиеся результаты
    if request.method == 'POST':
        student_id = request.form['id']
        student_results = models.Results.query.get(student_id)
        print(results)
        return render_template('results.html', results=student_results)