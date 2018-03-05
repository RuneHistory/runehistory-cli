from cement.core.foundation import CementApp
from runehistory_cli.framework.controllers.base import BaseController
from runehistory_cli.framework.controllers.highscore import HighScoreController
from runehistory_cli.framework.controllers.polling import PollingController


class RuneHistory(CementApp):
    class Meta:
        label = 'runehistory'
        handlers = [
            BaseController,
            HighScoreController,
            PollingController
        ]
