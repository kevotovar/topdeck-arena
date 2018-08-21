import requests

from django.conf import settings


class Challonge():

    def __init__(self):
        self.API_KEY = settings.CHALLONGE_API_KEY

    def _request(self, endpoint, params=dict(), data=dict(), method='GET'):
        url = 'https://api.challonge.com/v1/' + endpoint + '.json'
        params['api_key'] = self.API_KEY
        if method == 'GET':
            return requests(url, params=params)

    def get_available_tournaments(self, state=''):
        pass
