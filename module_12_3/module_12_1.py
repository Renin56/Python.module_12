import unittest
import runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run = runner.Runner('Mick')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rnr = runner.Runner('Alex')
        for _ in range(10):
           rnr.run()
        self.assertEqual(rnr.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = runner.Runner('Nick')
        run2 = runner.Runner('Bob')

        for _ in range(10):
            run1.walk()
            run2.run()

        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()
    