import logging
import rt_with_exceptions as runner
import unittest


logging.basicConfig(level = logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            run = runner.Runner('Mick',  -10)
            for _ in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            rnr = runner.Runner(12, 10)
            for _ in range(10):
               rnr.run()
            self.assertEqual(rnr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        run1 = runner.Runner('Nick')
        run2 = runner.Runner('Bob')

        for _ in range(10):
            run1.walk()
            run2.run()

        self.assertNotEqual(run1.distance, run2.distance)