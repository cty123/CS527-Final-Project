from GDBAction import GDBAction

START_SUCCESS = 0
START_ERROR = 1


class StartAction(GDBAction):
    def __init__(self, gdb):
        super().__init__(gdb)
        self.cmd = 'start'
        self.execute_command()

    def handle_result(self, data):
        if data['message'] == 'error':
            self.log_error(data['payload']['msg'])
            self.res = START_ERROR
        else:
            self.res = START_SUCCESS
