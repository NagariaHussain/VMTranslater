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
                code = f'''@{tokens['arg2']}
D = A
@SP
A = M
M = D
@SP
M = M + 1
'''
                self.out_stream.write(code)

        # If the command type is pop
        elif command_type == CommandType.C_POP:
            pass

    # Close the output file stream
    def close(self):
        self.out_stream.close()
