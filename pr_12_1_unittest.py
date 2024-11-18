print('Проверка на выносливость')

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    # Задание 1: test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод
    # walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    def test_walk(self):
        walker = Runner('Walker')
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    # Задание 2. test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run
    # у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    def test_run(self):
        runner = Runner('Runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    # Задание 3. test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10
    # раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод
    # assertNotEqual, чтобы убедится в неравенстве результатов.
    def test_challenge(self):
        runner = Runner('Champ')
        walker = Runner('Lagger')
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(100, 50, 'Champ must be 50 miters ahead of Lagger')


if __name__ == '__main__':
    unittest.main()
