from app import app
from app import subjects
from flask import (render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   )

from app import models
from .forms import IDForm

from collections import namedtuple


@app.route('/')
@app.route('/index')
def index():
    form = IDForm()
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        student_id = request.form['id']
        results = get_results(student_id)
        
        if results is None:
            flash('Участника с таким номером у нас нет. Попробуйте еще раз',
                  'warning')
            return redirect(url_for('index'))
        
        return render_template('results.html',
                               table=results.table,
                               student_id=student_id,
                               final=results.final
                               )
    else:
        return redirect(url_for('index'))


def get_results(student_id):
    student_results = models.Results.query.get(student_id)
    
    if not student_results:
        return None
    
    # Oh god why
    # TODO: make readable
    results_table = [(subjects.get(column).get('name'),
                      round(student_results[column], 1),
                      subjects.get(column).get('max_score'))
                     for column in student_results.__table__.columns.keys()
                     if student_results[column] is not None if
                     column in subjects]
    

    
    final = round(student_results.final, 1)
    results = namedtuple('results', ['table', 'final'])
    return results(results_table, final)
