from command_type import CommandType


class CodeWriter:
    '''Writes the assembly code that implements the parsed commands'''
    # constructor

    def __init__(self, out_path):
        self.out_stream = out_path.open("w")

    # Emits code for arithmetic
    def write_arithmetic(self, operation):
        pass

    # Emits code for push/pop
    def write_push_pop(self, command_type, tokens):
        # If the command type is push
        if command_type == CommandType.C_PUSH:
            if tokens['arg1'] == 'constant':
                # push constant i
                code = f'''// push constant {tokens['arg2']}
@{tokens['arg2']}
D = A
@SP
A = M
M = D
@SP
M = M + 1
''' 
            elif tokens['arg1'] == 'local':
                # push local i
                code = f'''// push local {tokens['arg2']}
@{tokens['arg2']}
D = A
@LCL 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
'''

        # If the command type is pop
        elif command_type == CommandType.C_POP:
            if tokens['arg1'] == 'local':
                code = f'''// pop local {tokens['arg2']}
@{tokens['arg2']}
D = A
@LCL
D = D + M
@SP
A = M
M = D
@SP
M = M - 1
@SP
D = M
A = A + 1
A = M
M = D
'''
        self.out_stream.write(code)
    # Close the output file stream
    def close(self):
        self.out_stream.close()
