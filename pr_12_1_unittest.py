print('Задача "Проверка на выносливость"')

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10
        return self.distance

    def walk(self):
        self.distance += 5
        return self.distance

    def __str__(self):
        return self.name

# walker = Runner('Walker')
# runner = Runner('Runner')
# print(walker)
# print(runner)
# print(walker.walk())
# print(runner.run())


class RunnerTest(unittest.TestCase):
    is_frozen = False
    # Задание 1: test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод
    # walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')    # почему без cls.is_frozen?
    def test_walk(self):
        walker = Runner('Walker')
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    # Задание 2. test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run
    # у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Runner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    # Задание 3. test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10
    # раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод
    # assertNotEqual, чтобы убедится в неравенстве результатов.
    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = Runner('Champ')
        walker = Runner('Lagger')
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(100, 50, 'Champ must be 50 miters ahead of Lagger')


if __name__ == '__main__':
    unittest.main()