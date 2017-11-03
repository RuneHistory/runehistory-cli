from cement.core.controller import CementBaseController, expose


class PollingController(CementBaseController):
    class Meta:
        label = 'poll'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = "Fetch player highscores in a long running process"
        arguments = [
            (
                ['-ul', '--unchanged-min', '--unchanged-low'],
                dict(
                    help='Minimum amount of unchanged runs',
                    dest='unchanged_min'
                )
            ),
            (
                ['-uh', '--unchanged-max', '--unchanged-high'],
                dict(
                    help='Maximum amount of unchanged runs',
                    dest='unchanged_max'
                )
            ),
            (
                ['-t', '--time'],
                dict(
                    help='Amount of time in minutes passed to get the same account',
                    dest='time'
                )
            ),
            (
                ['--api-host'],
                dict(
                    help='Runehistory api host',
                    dest='api_host',
                    default='http://api.runehistory.local/v1'
                )
            ),
        ]

    @expose(hide=True)
    def default(self):
        from runehistory.polling import start
        from runehistory.api import setup
        setup(self.app.pargs.api_host)
        time = self.app.pargs.time
        time = int(time) if time is not None else None
        start(self.app.pargs.unchanged_min, self.app.pargs.unchanged_max, time)
