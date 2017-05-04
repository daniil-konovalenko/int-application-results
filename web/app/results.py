from collections import namedtuple

from app.models import Student


def get_student(student_id):
    if not student_id.isdigit():
        return None
    
    student = Student.query.filter(Student.assigned_id == student_id).first()
    if not student:
        return None
    return student


def get_results(student_id):
    student = get_student(student_id)
    if not student:
        return None
    # TODO: custom formula
    # final = calculate_final(student.results)
    Results = namedtuple('Results', ['rows', 'final', 'normalized_present'])
    rows = get_result_rows(student)
    return Results(rows, calculate_final(student),
                   is_normalized_present(get_result_rows(student)))


def get_result_rows(student):
    ResultRow = namedtuple('ResultRow',
                           ['subject',
                            'score',
                            'str_score',
                            'normalized_score',
                            'is_significant'])
    
    student_results = student.results
    result_rows = []
    for result in student_results:
        if student.grade == 10:
            significant = False
        else:
            significant = is_significant(student_results, result)
    
        if result.subject.max_score is None:
            normalized_score = None
        else:
            normalized_score = result.score / result.subject.max_score * 20
    
        row = ResultRow(result.subject,
                        result.score,
                        result.score_string,
                        normalized_score,
                        significant)
        result_rows.append(row)
    return result_rows


def calculate_final(student):
    if student.grade == 10:
        return None
    
    result_rows = get_result_rows(student)
    return (sum([result.normalized_score for result in result_rows
                 if result.is_significant]))


def is_significant(results, result):
    if result.subject.always_count:
        return True

    results = [r for r in results if not r.subject.always_count]
    comparator = lambda r: r.score / r.subject.max_score
    return result in sorted(results, key=comparator, reverse=True)[:2]


def is_normalized_present(result_rows):
    return any([row.normalized_score for row in result_rows])
