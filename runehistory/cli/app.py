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


def run(argv=None):
    with RuneHistory(argv=argv) as app:
        app.run()
