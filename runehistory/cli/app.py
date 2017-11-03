from cement.core.exc import CaughtSignal
from cement.core.foundation import CementApp
from .controllers.base import BaseController
from .controllers.highscores import HighScoresController
from .controllers.polling import PollingController


class RuneHistory(CementApp):
    class Meta:
        label = 'runehistory'
        handlers = [
            BaseController,
            HighScoresController,
            PollingController
        ]


def run():
    with RuneHistory() as app:
        app.setup()
        try:
            app.run()
        except (KeyboardInterrupt, SystemExit, CaughtSignal):
            print('Exiting...')
        app.close()
