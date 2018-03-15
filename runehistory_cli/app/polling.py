from typing import Union
import datetime
from time import sleep

from ioccontainer import inject
from requests.exceptions import ConnectionError
from pyrunehistory.client import Client
from pyrunehistory.domain.models.account import Account

from runehistory_cli.domain.models.highscore import HighScore
from runehistory_cli.app.highscore import get


@inject('rh')
def start(unchanged_min: Union[int, None] = None,
          unchanged_max: Union[int, None] = None,
          time: Union[int, None] = None, rh: Client = None):

    while True:
        before_time = None if not time else \
            datetime.datetime.now() - datetime.timedelta(minutes=time)
        accounts = rh.accounts.get_accounts(unchanged_min, unchanged_max,
                                            before_time)
        if not len(accounts):
            sleep(10)
            continue
        for account in accounts:
            process_account(account)


@inject('rh')
def process_account(account: Account, rh: Client = None):
    highscore = get_highscore(account)
    rh.accounts.highscores(account.slug).create_highscore(highscore.skills)
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
