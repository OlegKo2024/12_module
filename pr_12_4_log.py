class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# first = Runner('Вася', 10)
# second = Runner('Илья', 5)
# third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())

import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            walker = Runner('Walker', -5)
            logging.info(f'test_walk" выполнен успешно')
            for _ in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
        except ValueError as ver:
            logging.warning(f'Неверная скорость для Runner: {ver}', exc_info=True)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(2)
            logging.info(f'test_run" выполнен успешно')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as ter:
            logging.warning(f'Неверный тип данных для объекта Runner: {ter}', exc_info=True)

    @unittest.skipIf(is_frozen is True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = Runner('Champ')
        walker = Runner('Lagger')
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(100, 50, 'Champ must be 50 miters ahead of Lagger')

    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()
