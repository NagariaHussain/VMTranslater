from command_type import CommandType


class CodeWriter:
    '''Writes the assembly code that implements the parsed commands'''
    # constructor

    def __init__(self, out_path):
        # Open output stream
        self.out_stream = out_path.open("w")

        # Get module base name
        self.file_name = out_path.stem

    # Emits code for arithmetic
    def write_arithmetic(self, operation):
        pass

    # Emits code for push/pop
    def write_push_pop(self, command_type, tokens):
        # Map segment type to base address pointer
        base = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT'
        }

        # If the command type is push
        if command_type == CommandType.C_PUSH:
            if tokens['arg1'] == 'constant':
                # push constant i
                code = f'''
// push constant {tokens['arg2']}
@{tokens['arg2']}
D = A
@SP
A = M
M = D
@SP
M = M + 1
''' 
            elif tokens['arg1'] in ('local', 'argument', 'this', 'that'):
                # push segment i
                code = f'''
// push {tokens['arg1']} {tokens['arg2']}
@{tokens['arg2']}
D = A
@{base[tokens['arg1']]} 
A = D + M
D = M
@SP
A = M
M = D
@SP
M = M + 1
'''
            elif tokens['arg1'] == 'static':
                # push static i
                code = f'''
// push static {tokens['arg2']}
@{self.file_name}.{tokens['arg2']}
D = M
@SP
A = M
M = D
@SP
M = M + 1
'''
        # If the command type is pop
        elif command_type == CommandType.C_POP:
            # pop segment i
            if tokens['arg1'] in ('local', 'argument', 'this', 'that'):
                code = f'''
// pop {tokens['arg1']} {tokens['arg2']}
@{tokens['arg2']}
D = A
@{base[tokens['arg1']]}
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
            elif tokens['arg1'] == 'static':
                # pop static i
                code = f'''
// pop static {tokens['arg2']}
@SP
M = M - 1
A = M
D = M

@{self.file_name}.{tokens['arg2']}
M = D
'''
        self.out_stream.write(code)
    # Close the output file stream
    def close(self):
        self.out_stream.close()
