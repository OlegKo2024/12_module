import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2
        return self.distance

    def walk(self):
        self.distance += self.speed
        return self.distance

    def __str__(self):
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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    def test_first_run(self):
        first_run = Tournament(90, self.runner1, self.runner3)
        results = first_run.start()
        TournamentTest.all_results[1] = results  # Сохраняем результаты первого теста
        self.assertEqual(results[max(results.keys())], 'Ник')

    def test_second_run(self):
        first_run = Tournament(90, self.runner2, self.runner3)
        results = first_run.start()
        TournamentTest.all_results[2] = results  # Сохраняем результаты второго теста
        self.assertEqual(results[max(results.keys())], 'Ник')

    def test_third_run(self):
        first_run = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = first_run.start()
        TournamentTest.all_results[3] = results  # Сохраняем результаты третьего теста
        self.assertEqual(results[max(results.keys())], 'Ник')

    @classmethod
    def tearDownClass(cls):
        for test_number, test_result in cls.all_results.items():
            print(test_result)

if __name__ == '__main__':
    unittest.main()