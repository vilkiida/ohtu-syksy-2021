import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub())
    
    def test_setup_works(self):
        pelaaja = self.statistics._players[0]
        pelaajan_nimi = pelaaja.name
        self.assertEqual(pelaajan_nimi, "Semenko")

    def test_search_with_right_imput_works(self):
        pelaaja = self.statistics.search("Semenko")
        self.assertEqual(pelaaja.goals, 4)
    
    def test_search_with_wrong_imput_works(self):
        pelaaja = self.statistics.search("Wrong")
        self.assertEqual(pelaaja, None)
    
    def test_team_works_with_right_imput(self):
        tiimi = self.statistics.team("EDM")
        pelaaja1 = tiimi[0]

        self.assertEqual(pelaaja1.name, "Semenko")
    
    def test_teams_works_with_wrong_imput(self):
        tiimi = self.statistics.team("Wrong")
        self.assertEqual(tiimi, [])
    
    def test_top_scorers_works_the_way_is_supposed_to(self):
        tulokset = self.statistics.top_scorers(2)
        paras = tulokset[0]
        self.assertEqual(paras.name, "Gretzky")
