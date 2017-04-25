from app.models import Student

from collections import namedtuple


def get_results(student_id):
    if not student_id.isdigit():
        return None
    
    student = Student.query.filter(Student.assigned_id == student_id).first()
    
    if not student:
        return None
    
    results_table = [(result.subject.name,
                      result.score,
                      result.subject.max_score)
                     for result in student.results]
    
    # TODO: custom formula
    final = calculate_final(student.results)
    results = namedtuple('results', ['table', 'final'])
    return results(results_table, final)


def calculate_final(results):
    return sum([result.score for result in results])
