import click

from runehistory_cli.app.polling import start


@click.command()
@click.option('--umin', default=None, help='Minimum amount of times an account has been unchanged.')
@click.option('--umax', default=None, help='Maxiumum amount of times an account has been unchanged.')
@click.option('-t', default=10, help='Amount of time in minutes passed to get the same account.')
def poll(umin, umax, t):
    umin = int(umin) if umin else None
    umax = int(umax) if umax else None
    time = int(t) if t else None
    start(umin, umax, time)
