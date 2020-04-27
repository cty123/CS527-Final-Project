from graphviz import Digraph


def create_node(name, params, addr, in_reg, out_reg):

    return f'''<
    <table border="0">
        <tr><td align="text" border="1">{name}</td></tr>
        <tr><td align="text">addr: {addr}</td></tr>
        <tr><td align="text">params: {params}</td></tr>
        <tr><td align="text" border="1">Entrance Registers</td></tr>
        <tr><td align="text">rdi: {in_reg.get('rdi')}</td></tr>
        <tr><td align="text">rsi: {in_reg.get('rsi')}</td></tr>
        <tr><td align="text">rdx: {in_reg.get('rdx')}</td></tr>
        <tr><td align="text">rcx: {in_reg.get('rcx')}</td></tr>
        <tr><td align="text">r8: {in_reg.get('r8')}</td></tr>
        <tr><td align="text">r9: {in_reg.get('r9')}</td></tr>
        <tr><td align="text">rip: {in_reg.get('rip')[0] if in_reg.get('rip') is not None else None}</td></tr>
        <tr><td align="text" border="1">Entrance Registers</td></tr>
        <tr><td align="text">rax: {out_reg.get('rax')}</td></tr>
    </table>
    >'''


def draw_uml(s):
    # Vertex Counter
    ctr = 1
    # Create Digraph
    dot = Digraph(format="png")
    # Create Main Node
    dot.node(s.name, create_node(s.name, s.params, s.addr, s.entrance_registers, s.exit_registers), shape="box")
    # Create DFS_Stack
    dfs_stack = [(s.name, s)]
    # Loop
    while len(dfs_stack) != 0:
        (curr_name, curr) = dfs_stack.pop()
        if len(curr.call_functions) != 0:
            for i in curr.call_functions:
                name = f'{curr.name}_{curr.addr}_{ctr}'
                dot.node(name, create_node(i.name, i.params, i.addr, i.entrance_registers, i.exit_registers),
                         shape="box")
                dot.edge(curr_name, name)
                dfs_stack.append((name, i))
                ctr += 1

    dot.render('./Out/result.gv', view=True)
