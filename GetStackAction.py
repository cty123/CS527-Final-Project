from GDBAction import GDBAction


class GetStackAction(GDBAction):
    def __init__(self, gdb):
        super().__init__(gdb)
        self.cmd = "bt"
        self.res = {}
        self.execute_command()

    def handle_console(self, data):
        # Parse stack info
        payload = data['payload'].replace('\\n', '').split()

        # Get stack number
        num = int(payload[0][1:])

        # Check if the break function is external function
        if "(format=" in payload[2]:
            func_name = payload[1]
            addr = payload[2].replace("(format=", "")
            args = "None"
        else:
            payload = data['payload'].replace('\\n', '').split()

            # Parse data
            addr = payload[1]
            func_name = payload[3]
            args = payload[4]

        self.res[num] = (addr, func_name, args)
