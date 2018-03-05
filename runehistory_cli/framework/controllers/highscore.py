import json

from cement.core.controller import CementBaseController, expose
from ioccontainer import inject

from runehistory_cli.app.api import RuneHistoryApi
from runehistory_cli.app.highscore import get


class HighScoreController(CementBaseController):
    class Meta:
        label = 'highscore'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Fetch player highscores'
        arguments = [
            (
                ['-p', '--player'],
                dict(help='Player name', dest='player', required=True)
            ),
            (
                ['--api-host'],
                dict(
                    help='Runehistory api host',
                    dest='api_host',
                    default='http://api.runehistory.com/v1'
                )
            ),
        ]

    @expose(hide=True)
    @inject('rhapi')
    def default(self, rhapi: RuneHistoryApi):
        rhapi.host = self.app.pargs.api_host
        account = rhapi.get_account(self.app.pargs.player)
        highscore = get(account)
        print(json.dumps(highscore.get_encodable()))
