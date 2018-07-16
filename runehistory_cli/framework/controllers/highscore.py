import json

import click
from ioccontainer import inject
from pyrunehistory.client import Client
from pyrunehistory.osrs import get_highscore


@click.command()
@click.argument('slug')
@inject('rh')
def highscore(rh: Client, slug):
    account = rh.accounts.get_account(slug)
    highscore = get_highscore(account)
    print(json.dumps(highscore.get_encodable()))
