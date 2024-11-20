import unittest
import module_12_1
import module_12_2


runTS = unittest.TestSuite()

runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runTS.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTS)
