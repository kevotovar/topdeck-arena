import unittest
from .challonge import Challonge


class TestChallongeService(unittest.TestCase):

    def setUp(self):
        self.challonge_service = Challonge()

    def test_get_available_tournaments(self):
        self.assertTrue(self.challonge_service.get_available_tournaments())
