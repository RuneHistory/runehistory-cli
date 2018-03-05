import json
import typing

import requests
from ioccontainer import provider, scopes

from runehistory_core.domain.models.account import Account
from runehistory_core.domain.models.highscore import HighScore
from runehistory_core.app.repositories.highscore import HighScoreRepository


def get_raw_highscores(player: str) -> str:
    response = requests.get(
        'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws', {
            'player': player
        })
    response.raise_for_status()
    return response.content.decode('utf-8')


class RuneHistoryApi(object):
    def __init__(self, host: str = None):
        self.host = host

    def get_account(self, slug: str) -> Account:
        response = self._request(
            'GET',
            'accounts/{}'.format(slug)
        )
        return Account(**response.json())

    def get_accounts(self, unchanged_min: typing.Union[int, None] = None,
                     unchanged_max: typing.Union[int, None] = None,
                     before_time: typing.Union[int, None] = None) -> typing.List:
        response = self._request(
            'GET',
            'accounts',
            params={
                'prioritise': True,
                'runs_unchanged_min': unchanged_min,
                'runs_unchanged_max': unchanged_max,
                'last_ran_before': before_time,
            }
        )
        accounts = []
        for record in response.json():
            accounts.append(Account(**record))
        return accounts

    def post_highscores(self, account: Account, highscore: HighScore) -> HighScore:
        data = highscore.get_encodable()
        response = self._request(
            'POST',
            'accounts/{slug}/highscores'.format(
                slug=account.slug
            ),
            data=data
        )
        return HighScoreRepository.from_record(response.json())

    def _request(self, method: str, url: str, params: typing.Dict = None,
                 data: typing.Dict = None) -> requests.Response:
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


@provider(RuneHistoryApi, scopes.SINGLETON)
def provide_rh_api():
    return RuneHistoryApi()
