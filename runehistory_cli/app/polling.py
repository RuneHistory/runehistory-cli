from typing import Union
import datetime
from time import sleep

from ioccontainer import inject
from requests.exceptions import ConnectionError
from runehistory_core.domain.models.account import Account
from runehistory_core.domain.models.highscore import HighScore

from runehistory_cli.app.api import RuneHistoryApi
from runehistory_cli.app.highscore import get


@inject('rhapi')
def start(unchanged_min: Union[int, None] = None,
          unchanged_max: Union[int, None] = None,
          time: Union[int, None] = None, rhapi: RuneHistoryApi = None):

    while True:
        before_time = time if time is None else \
            datetime.datetime.now() - datetime.timedelta(minutes=time)
        accounts = rhapi.get_accounts(unchanged_min, unchanged_max, before_time)
        if not len(accounts):
            sleep(10)
            continue
        for account in accounts:
            process_account(account)


@inject('rhapi')
def process_account(account: Account, rhapi: RuneHistoryApi = None):
    highscore = get_highscore(account)
    rhapi.post_highscores(account, highscore)
    print('Processed {nickname} ({slug})'.format(
        nickname=account.nickname,
        slug=account.slug,
    ))


def get_highscore(account: Account) -> HighScore:
    while True:
        try:
            return get(account)
        except ConnectionError:
            sleep(10)
