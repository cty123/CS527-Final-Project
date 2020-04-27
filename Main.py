from pygdbmi.gdbcontroller import GdbController

from BreakPointAction import BreakPointAction
from GetStackAction import GetStackAction
from ProgramController import ProgramController
from StartAction import StartAction


def start_program(gdb):
    start_res = gdb.write("start")
    for data in start_res:
        if data['type'] == 'result' and data['message'] == 'running':
            return GetStackAction(gdb)
    return None


if __name__ == '__main__':
    # Define program and watch list
    file_name = "./Test/simple_test1"
    watch_list = ["func1", "func2", "func3", "printf", "puts"]

    # Start execution
    gdb = GdbController()
    res = gdb.write("file " + file_name)

    # Set break points
    for f in watch_list:
        BreakPointAction(gdb, f)

    # Start Program execution
    program = ProgramController(gdb)
    program.start()
