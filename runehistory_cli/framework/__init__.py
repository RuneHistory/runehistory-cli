import click
from ioccontainer import provider, scopes
from pyrunehistory.client import Client

from runehistory_cli.framework.controllers.highscore import highscore
from runehistory_cli.framework.controllers.poll import poll


@click.group()
@click.option('--host', default=None, help='RuneHistory API host')
def cli(host):
    @provider(Client, scopes.SINGLETON)
    def provide_rh_client():
        args = {}
        if host:
            args['host'] = host
        return Client(**args)


cli.add_command(highscore)
cli.add_command(poll)
