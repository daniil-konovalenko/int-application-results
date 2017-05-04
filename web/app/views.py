from flask import (render_template,
                   request,
                   redirect,
                   url_for,
                   flash,
                   )

from app import app
from .forms import IDForm
from .results import get_results


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
                               results=results.rows,
                               student_id=student_id,
                               final=results.final,
                               show_normalized=results.normalized_present
                               )
    else:
        return redirect(url_for('index'))
