from GDBAction import GDBAction


class GetStackAction(GDBAction):
    def __init__(self, gdb):
        super().__init__(gdb)
        self.cmd = "bt"
        self.res = {}
        self.execute_command()

    def handle_console(self, data):
        payload = data['payload'].replace('\\n', '').split()

        # Parse data
        num = int(payload[0][1:])
        addr = payload[1]
        func_name = payload[3]
        args = payload[4]
        self.res[num] = (addr, func_name, args)
