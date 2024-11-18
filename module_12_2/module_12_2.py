import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = rat.Runner('Усэйн', 10)
        self.runner2 = rat.Runner('Андрей', 9)
        self.runner3 = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in range(0, len(TournamentTest.all_results)):
            print(TournamentTest.all_results[i])

    def test_first_tournament(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_second_tournament(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_third_tournament(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
