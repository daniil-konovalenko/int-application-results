from app import app
from flask import (render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   )
from .forms import IDForm
from app import models
from app import subjects

@app.route('/')
@app.route('/index')
def index():
    form = IDForm()
    return render_template('index.html', form=form)


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        student_id = request.form['id']
        student_results = models.Results.query.get(student_id)

        if not student_results:
            flash('Кажется, участника с таким номером у нас нет. Попробуйте еще раз', 'warning')
            return redirect(url_for('index'))

        results_table = [(subjects.get(column), student_results[column])
                         for column in student_results.__table__.columns.keys()
                         if student_results[column] is not None if column in subjects]


        return render_template('results.html',
                               table=results_table,
                               student_id=student_id,
                               comments=student_results.comments)

    else:
        return redirect(url_for('index'))
