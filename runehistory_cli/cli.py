from cement.core.exc import CaughtSignal

from runehistory_cli.framework import RuneHistory


def run():
    with RuneHistory() as app:
        app.setup()
        try:
            app.run()
        except (KeyboardInterrupt, SystemExit, CaughtSignal):
            print('Exiting...')
        app.close()


if __name__ == '__main__':
    run()
