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
            flash('Кажется, участника с таким номером у нас нет. Попробуйте еще раз',
                  'warning')
            return redirect(url_for('index'))

        results_table = [(subjects.get(column).get('name'),
                          student_results[column],
                          subjects.get(column).get('max_score'))
                         for column in student_results.__table__.columns.keys()
                         if student_results[column] is not None if column in subjects]

        normalized_math_test = student_results.math_test / 13 * 20
        sum_of_two_best = sum(sorted([result[1] for result in results_table[1:]],
                                     reverse=True)[:2])

        final = "{:.1f}".format(normalized_math_test + sum_of_two_best)

        return render_template('results.html',
                               table=results_table,
                               student_id=student_id,
                               final=final
                               )

    else:
        return redirect(url_for('index'))
