import datetime
from runehistory.highscores import get, HighScores
from runehistory.api import api
from typing import Union
from runehistory.utils import to_dict
from time import sleep
from requests.exceptions import ConnectionError


def start(unchanged_min: Union[int, None] = None,
          unchanged_max: Union[int, None] = None,
          time: Union[int, None] = None):

    while True:
        before_time = time if time is None else \
            datetime.datetime.now() - datetime.timedelta(minutes=time)
        accounts = api.get_accounts(unchanged_min, unchanged_max, before_time)
        if not len(accounts):
            sleep(10)
            continue
        for account in accounts:
            process_account(account)


def process_account(account: dict):
    highscores = get_highscores(account['nickname'])
    api.post_highscores(account['slug'], to_dict(highscores))
    print('Processed {nickname} ({slug})'.format(
        nickname=account['nickname'],
        slug=account['slug'],
    ))


def get_highscores(nickname: str) -> HighScores:
    while True:
        try:
            return get(nickname)
        except ConnectionError:
            sleep(10)
