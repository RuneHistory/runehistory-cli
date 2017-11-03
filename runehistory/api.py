import requests
import json
from typing import Union


def get_raw_highscores(player: str) -> str:
    response = requests.get(
        'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
            'player': player
        })
    response.raise_for_status()
    return response.content.decode('utf-8')


class RuneHistoryApi(object):
    def __init__(self):
        self.host = None

    def get_accounts(self, unchanged_min: Union[int, None] = None,
                     unchanged_max: Union[int, None] = None,
                     before_time: Union[int, None] = None) -> dict:
        response = self._request(
            'GET',
            'accounts',
            params={
                'prioritise': True,
                'runsUnchangedMin': unchanged_min,
                'runsUnchangedMax': unchanged_max,
                'lastRanBefore': before_time,
            }
        )
        return response.json()['data']

    def post_highscores(self, slug: str, highscores: dict) -> dict:
        data = {'skills': highscores}
        response = self._request(
            'POST',
            'accounts/{slug}/highscores'.format(
                slug=slug
            ),
            data=data
        )
        return response.json()['data']

    def _request(self, method: str, url: str, params: Union[dict, None] = None,
                 data: Union[dict, None] = None) -> requests.Response:
        url = '{host}/{endpoint}'.format(
            host=self.host,
            endpoint=url
        )
        encoded_data = json.dumps(data)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.request(method, url, params=params,
                                    data=encoded_data, headers=headers)
        response.raise_for_status()
        return response


def setup(host: str):
    api.host = host


api = RuneHistoryApi()
