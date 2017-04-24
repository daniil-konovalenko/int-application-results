import logging

from web.app import db
from web.app import subjects

from web.app import models


def final_score(result, math_test, math_test_max_score):
    results_table = [(subjects.get(column).get('name'),
                        result[column],
                          subjects.get(column).get('max_score'))
                          for column in result.__table__.columns.keys()
                          if result[column] is not None if column in subjects]

    normalized_math_test = result[math_test] / math_test_max_score * 20
    sum_of_two_best = sum(sorted([result[1] for result in results_table[1:]],
                                     reverse=True)[:2])

    final = round(sum_of_two_best + normalized_math_test, 1)
    return final


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    for result in models.Results.query.all():
        logging.info("Procesing ", result)


        try:

            final = final_score(result, "math_test", 13)
            result.final = final
        except TypeError as e:
            logging.error(e)
    db.session.commit()
    logging.info("Finished")
