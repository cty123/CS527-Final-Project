# Define types of messages
MESSAGE_TYPE_RESULT = 'result'
MESSAGE_TYPE_LOG = 'log'
MESSAGE_TYPE_NOTIFY = 'notify'
MESSAGE_TYPE_CONSOLE = 'console'


class GDBAction:

    def __init__(self, gdb):
        self.gdb = gdb
        self.res = None

    def perform_action(self):
        return self.gdb.write(self.cmd)

    def execute_command(self):
        res = self.perform_action()
        for data in res:
            if data['type'] == MESSAGE_TYPE_RESULT:
                self.handle_result(data)
            elif data['type'] == MESSAGE_TYPE_LOG:
                self.handle_log(data)
            elif data['type'] == MESSAGE_TYPE_NOTIFY:
                self.handle_notify(data)
            elif data['type'] == MESSAGE_TYPE_CONSOLE:
                self.handle_console(data)

    def handle_result(self, data):
        pass

    def handle_log(self, data):
        self.log(data['payload'])

    def handle_notify(self, data):
        pass

    def handle_console(self, data):
        self.log_console(data['payload'])

    def log(self, msg):
        print("GDB Command Action: " + msg)

    def log_console(self, msg):
        print("GDB Console Output: " + msg)

    def log_error(self, msg):
        print("GDB Action Error: " + msg)