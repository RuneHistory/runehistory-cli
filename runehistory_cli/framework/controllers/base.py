from cement.core.controller import CementBaseController, expose


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'RuneHistory CLI application to pull player highscores'

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()
