import datetime
from runehistory.highscores import get
from runehistory.api import api
from typing import Union
from runehistory.utils import to_dict


def start(unchanged_min: Union[int, None] = None,
          unchanged_max: Union[int, None] = None,
          time: Union[int, None] = None):
    before_time = time if time is None else \
        datetime.datetime.now() - datetime.timedelta(minutes=time)

    while True:
        accounts = api.get_accounts(unchanged_min, unchanged_max, before_time)
        for account in accounts:
            process_account(account)
        break  # TODO: Stop breaking the loop


def process_account(account: dict):
    highscores = get(account['nickname'])
    api.post_highscores(account['slug'], to_dict(highscores))
    print('Processed {nickname} ({slug})'.format(
        nickname=account['nickname'],
        slug=account['slug'],
    ))
