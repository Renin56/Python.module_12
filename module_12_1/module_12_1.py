import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = runner.Runner('Maxim')
        for i in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = runner.Runner('Ivan')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run3 = runner.Runner('Vladimir')
        run4 = runner.Runner('Oleg')
        for i in range(10):
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance)


if __name__ == '__main__':
    unittest.main()

