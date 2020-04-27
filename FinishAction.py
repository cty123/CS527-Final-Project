from GDBAction import GDBAction


FINISH_BREAKPOINT = 0
FINISH_MAIN = 1


class FinishAction(GDBAction):
    def __init__(self, gdb):
        super().__init__(gdb)
        self.cmd = 'finish'
        self.execute_command()

    def handle_result(self, data):
        if data['message'] == 'running':
            self.res = FINISH_BREAKPOINT
        else:
            self.res = FINISH_MAIN
