from BreakPointAction import BreakPointAction
from ContinueAction import ContinueAction, PROGRAM_BREAKPOINT
from FinishAction import FinishAction, FINISH_MAIN
from GetStackAction import GetStackAction
from RegisterAction import RegisterAction
from StartAction import StartAction, START_SUCCESS
from Graphviz import draw_uml


class FunctionCall:
    def __init__(self, addr, name, params, caller):
        self.name = name
        self.params = params
        self.addr = addr
        self.caller = caller
        self.call_functions = []
        self.entrance_registers = {}
        self.exit_registers = {}


class ProgramController:
    def __init__(self, gdb, watch_list, input_file):
        self.gdb = gdb
        # Initialize call stack
        main_func = FunctionCall("0xmain", "main", [], None)
        self.last_func = main_func
        self.stack = main_func
        self.watch_list = watch_list
        self.input_file = input_file

    def start(self):
        # Start Program
        start_status = StartAction(self.gdb, self.input_file).res
        if start_status != START_SUCCESS:
            print("Error... Exiting")

        # Set break points
        for f in self.watch_list:
            BreakPointAction(self.gdb, f)

        # Continue to next function
        continue_status = ContinueAction(self.gdb).res

        # While the program doesn't exit
        while continue_status == PROGRAM_BREAKPOINT:
            # Get call stack
            call_stack = GetStackAction(self.gdb).res

            # Get register info
            registers = RegisterAction(self.gdb).res

            # Update call stack record
            temp = self.last_func
            add_flag = False
            function_list = list(call_stack.values())
            function_list.reverse()
            for addr, func_name, params in function_list:
                if add_flag:
                    func = FunctionCall(addr, func_name, [], temp)
                    temp.call_functions.append(func)
                    temp = func

                if func_name == self.last_func.name:
                    add_flag = True

            # Update last_func
            if add_flag:
                self.last_func = temp
                self.last_func.entrance_registers = registers
            else:
                self.last_func.exit_registers = registers
                self.last_func = self.last_func.caller

            finish_status = FinishAction(self.gdb).res
            if finish_status == FINISH_MAIN:
                continue_status = ContinueAction(self.gdb).res
            else:
                continue_status = PROGRAM_BREAKPOINT

        # Print out stack
        self.print_stack(self.stack)

        # Generate UML graph
        draw_uml(self.stack)

    def print_stack(self, s):
        if len(s.call_functions) != 0:
            for i in s.call_functions:
                print(f'{s.addr}_{s.name}_{s.params}', end=' ')
                print('->', end=' ')
                self.print_stack(i)
        else:
            print(f'{s.addr}_{s.name}_{s.params}')
