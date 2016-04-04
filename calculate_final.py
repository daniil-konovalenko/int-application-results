from app import db
from app import models
from app import subjects
import logging


math_max = 13

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    for result in models.Results.query.all():
        logging.info("Procesing ", result)

        results_table = [(subjects.get(column).get('name'),
                        result[column],
                          subjects.get(column).get('max_score'))
                          for column in result.__table__.columns.keys()
                          if result[column] is not None if column in subjects]

        try:
            normalized_math_test = result.math_test / math_max * 20
            sum_of_two_best = sum(sorted([result[1] for result in results_table[1:]],
                                     reverse=True)[:2])

            final = round(sum_of_two_best + normalized_math_test, 1)
            result.final = final


        except TypeError as e:
            logging.error(e)
            logging.error(results_table)

    db.session.commit()
    logging.info("Finished")
