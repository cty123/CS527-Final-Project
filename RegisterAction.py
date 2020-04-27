from GDBAction import GDBAction, MESSAGE_TYPE_RESULT, MESSAGE_TYPE_CONSOLE


class RegisterAction(GDBAction):
    def __init__(self, gdb):
        super().__init__(gdb)
        self.cmd = "i r"
        self.res = {}
        self.execute_command()

    def execute_command(self):
        res = self.perform_action()

        console_output = []

        # Check if the command is successful
        flag = False
        for data in res:
            if data['type'] == MESSAGE_TYPE_RESULT and data['message'] == 'done':
                flag = True
            elif data['type'] == MESSAGE_TYPE_CONSOLE:
                console_output.append(data['payload'])

        if not flag:
            return

        for i in range(0, len(console_output), 3):
            r, r_addr = console_output[i].split()
            value = console_output[i+1].replace('\\t', '')
            self.res[r] = (r_addr, value)
