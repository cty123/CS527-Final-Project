from GDBAction import GDBAction

PROGRAM_BREAKPOINT = 0
PROGRAM_EXIT = 1


class ContinueAction(GDBAction):
    def __init__(self, gdb):
        super().__init__(gdb)
        self.cmd = 'continue'
        self.execute_command()

    def handle_result(self, data):
        if data['message'] == 'running':
            self.res = PROGRAM_BREAKPOINT
        else:
            self.res = PROGRAM_EXIT
