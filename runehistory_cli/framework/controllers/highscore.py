import json

import click
from ioccontainer import inject
from pyrunehistory.client import Client

from runehistory_cli.app.highscore import get


@click.command()
@click.argument('slug')
@inject('rh')
def highscore(rh: Client, slug):
    account = rh.accounts.get_account(slug)
    highscore = get(account)
    print(json.dumps(highscore.get_encodable()))
