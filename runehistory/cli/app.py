from cement.core.foundation import CementApp
from .controllers.base import BaseController
from .controllers.highscores import HighScoresController


class RuneHistory(CementApp):
    class Meta:
        label = 'runehistory'
        handlers = [
            BaseController,
            HighScoresController
        ]


def run(argv=None):
    with RuneHistory(argv=argv) as app:
        app.run()
