from app import app
from flask import render_template, request
from .forms import IDForm
from app import models
from app import transcription

@app.route('/')
@app.route('/index')
def index():
    form = IDForm()
    return render_template('index.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        student_id = request.form['id']
        student_results = models.Results.query.get(student_id)
        results_table = [(transcription[column], student_results[column])
                         for column in student_results.__table__.columns.keys()
                         if student_results[column]]

        return render_template('results.html', results=results_table)

