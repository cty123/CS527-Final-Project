from GDBAction import GDBAction


class BreakPointAction(GDBAction):
    def __init__(self, gdb, func_name):
        super().__init__(gdb)
        self.func_name = func_name
        self.cmd = "break " + func_name
        self.execute_command()

    def handle_result(self, data):
        if data['message'] != 'done':
            print("Error: " + data['message'])
        else:
            print("Successfully set the break point to:", self.func_name)
