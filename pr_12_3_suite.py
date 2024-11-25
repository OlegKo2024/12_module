
import unittest
import pr_12_1_unittest
import pr_12_2_unittest

print('Задача "Заморозка кейсов"')

suite_tests = unittest.TestSuite()

suite_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(pr_12_1_unittest.RunnerTest))
suite_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(pr_12_2_unittest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_tests)

