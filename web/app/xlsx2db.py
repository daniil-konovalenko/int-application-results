import argparse
import logging

import pandas as pd

from app import db, app
from app.excel_processing import get_subjects
from app.models import Subject, Student, Result

parser = argparse.ArgumentParser(
    description='Move from excel table to sqlite3 db')
parser.add_argument('-f',
                    action='store',
                    required=True,
                    help='An xlsx file to extract data from')
parser.add_argument('-c',
                    action='store',
                    required=True,
                    help='Grade')

app.config.from_object('config.LoadResultsConfigLocal')

if __name__ == '__main__':
    path = r"C:\Users\ddkon\Desktop\результаты\10grade.xlsx"
    grade = 10
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # args = parser.parse_args()
    # path = args.f
    # grade = args.c
    
    df = pd.read_excel(path)
    subjects_names = get_subjects(df)
    print(f'Предметы: {subjects_names}')
    print(f'Загрузка результатов {grade} класса из {path}')
    print(f' в {app.config["SQLALCHEMY_DATABASE_URI"]}')
    
    while True:
        choice = input('Продолжить? (y/n): ')
        if choice.lower() not in {'y', 'n'}:
            continue
        if choice.lower() == 'y':
            break
        else:
            exit('Отменено пользователем')
    
    # subjects = {sname: Subject.query.filter(name=sname, grade=grade).first()
    #             for sname in subjects_strings}
    
    for index, row in df.iterrows():
        print(f'Ряд {index} из {len(df)}')
        student_id = int(row['ID'])
        
        student = Student(assigned_id=student_id, year=2017)
        db.session.add(student)
        
        for subject_name in subjects_names:
            score = row[subject_name]
            
            if pd.isnull(score):
                continue
            
            subject = db.session.query(Subject).filter_by(name=subject_name,
                                                          grade=grade).first()
            if not subject:
                print(f'Предмета "{subject_name}" нет')
                
                subject = Subject(name=subject_name, max_score=20, grade=grade)
                db.session.add(subject)
            
            try:
                score = float(score)
                result = Result(student=student, score=score, subject=subject,
                                grade=grade)
            except ValueError:
                score = str(score)
                result = Result(student=student, score_string=score,
                                subject=subject, grade=grade)
            
            db.session.add(result)
            print(f'Заполнил результат #{student_id} по {subject_name} '
                  f'в {score} баллов')
    
    db.session.commit()
