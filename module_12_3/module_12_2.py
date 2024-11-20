import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.Useyn = rat.Runner('Усейн', 10)
        self.Andrey = rat.Runner('Андрей', 9)
        self.Nick = rat.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in range(0, len(TournamentTest.all_results)):
            print(TournamentTest.all_results[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = rat.Tournament(90, self.Useyn, self.Nick)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = rat.Tournament(90, self.Andrey, self.Nick)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = rat.Tournament(90, self.Useyn, self.Andrey, self.Nick)
        result = tournament.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
