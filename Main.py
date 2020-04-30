from pygdbmi.gdbcontroller import GdbController

from BreakPointAction import BreakPointAction
from ProgramController import ProgramController
import sys


if __name__ == '__main__':

    # Check if arguments are passed
    if len(sys.argv) < 3:
        print("To use this program, run with\n\n \tpython3 Main.py [Program Name] [Monitor Function list] [Input "
              "file]\n")
        exit(1)

    # Get the name of the analyzed function and function list
    program_name = sys.argv[1]
    function_file = sys.argv[2]
    input_file = None

    if len(sys.argv) > 3:
        input_file = sys.argv[3]

    # Get function watch list
    watch_list = []
    with open(function_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            watch_list.append(line.replace('\n', ''))

    # Start execution
    gdb = GdbController()
    res = gdb.write("file " + program_name)

    # Set break points
    for f in watch_list:
        BreakPointAction(gdb, f)

    # Start Program execution
    program = ProgramController(gdb, input_file)
    program.start()
