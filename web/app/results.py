from app.models import Student, Subject

from collections import namedtuple


def get_results(student_id):
    if not student_id.isdigit():
        return None
    
    student = Student.query.filter(Student.assigned_id == student_id).first()
    math_test = Subject.query.filter(Subject.name.like('%тест%')).first()
    if not student:
        return None
    
    # TODO: custom formula
    # final = calculate_final(student.results)
    ResultRow = namedtuple('ResultRow',
                           ['subject',
                            'score',
                            'normalized_score',
                            'is_significant'])
    
   
    student_results = student.results
    
    results = [ResultRow(result.subject,
                         result.score,
                         result.score / result.subject.max_score * 20,
                         is_significant(student_results, result))
               for result in student_results]
    
        
    return results


def calculate_final(result_rows):
    return (sum([result.normalized_score for result in result_rows
                if result.is_significant]))


def is_significant(results, result):
    if result.subject.always_count:
        return True
    results = [r for r in results if not r.subject.always_count]
    comparator = lambda r: r.score / r.subject.max_score
    return result in sorted(results, key=comparator, reverse=True)[:2]