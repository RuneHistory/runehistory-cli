import click
from ioccontainer import provider, scopes
from pyrunehistory.client import Client

from runehistory_cli.framework.controllers.highscore import highscore
from runehistory_cli.framework.controllers.poll import poll


@click.group()
@click.option('--host', default=None, help='RuneHistory API host')
@click.option('--username', envvar='RH_USERNAME', help=)
@click.option('--password', envvar='RH_PASSWORD', help=)
@click.option('--secret', envvar='RH_SECRET', help=)
def cli(host, username, password, secret):
    @provider(Client, scopes.SINGLETON)
    def provide_rh_client():
        args = {}
        if host:
            args['host'] = host
        return Client(username, password, secret, **args)


cli.add_command(highscore)
cli.add_command(poll)
