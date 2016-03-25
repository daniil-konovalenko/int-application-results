from app import models
from app import db
from openpyxl import load_workbook
import argparse

parser = argparse.ArgumentParser(description='Move from excel table to sqlite3 db')
parser.add_argument('-f',
                    action='store',
                    required=True,
                    help='An xlsx file to extract data from')

if __name__ == '__main__':
    args = parser.parse_args()
    workbook = load_workbook(args.f)
    worksheet = workbook.active

    highest_column = worksheet.get_highest_column()
    highest_row = worksheet.get_highest_row()

    column_names = [cell.value.lower() for cell in list(worksheet.iter_rows())[0]]
    for row in worksheet.iter_rows(row_offset=1):
        (student_id,
         math_test,
         math,
         philology,
         history,
         science,
         comments) = [cell.value for cell in row]


        results = models.Results(student_id=student_id,
                                 math_test=math_test,
                                 math=math,
                                 philology=philology,
                                 history=history,
                                 science=science,
                                 comments=comments)

        db.session.add(results)

    db.session.commit()
