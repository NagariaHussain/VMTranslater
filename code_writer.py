from command_type import CommandType


class CodeWriter:
    '''Writes the assembly code that implements the parsed commands'''
    # constructor

    def __init__(self, out_path):
        # Open output stream
        self.out_stream = out_path.open("w")

        # Get module base name
        self.file_name = out_path.stem

        # Store operations count for each arithmetic operation
        # Helps in given Unique jump blocks
        self.op_count = {
            "eq": 0,
            "gt": 0,
            "lt": 0
        }

    # Emits code for arithmetic
    def write_arithmetic(self, operation):
        if operation == "add":
            code = f'''
// add
@SP
M=M-1
A=M
D = M
@SP
M = M - 1
A = M
M = D + M
@SP
M = M + 1
''' 
        elif operation == "sub":
            code = f'''
// sub
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
M = M - D
@SP
M = M + 1
'''
        elif operation == "neg":
            code = f'''
// neg
@SP
M = M - 1
A = M
M = -M

@SP
M = M + 1
'''
        elif operation == "eq":
            code = f'''
// eq
@SP
M = M-1
A = M
D = M
// D becomes y

@SP
M = M-1
A = M
D = M-D

// D becomes x - y
@TRUE_eq_{self.op_count['eq']}
// Jump if x == y
D;JEQ

// Jump unconditionally
@FALSE_eq_{self.op_count['eq']}
0;JMP

(TRUE_eq_{self.op_count['eq']})
@SP
A = M
M = -1

@END_eq_{self.op_count['eq']}
0;JMP

(FALSE_eq_{self.op_count['eq']})
@SP
A = M
M = 0

(END_eq_{self.op_count['eq']})
// SP++;
@SP
M = M + 1
'''         
            self.op_count['eq'] += 1
        elif operation == "gt":
            code = f'''
// gt
@SP
M = M-1
A = M
D = M
// D becomes y

@SP
M = M-1
A = M
D = M-D

// D becomes x - y
@TRUE_gt_{self.op_count['gt']}
// Jump if x > y
D;JGT

// Jump unconditionally
@FALSE_gt_{self.op_count['gt']}
0;JMP

(TRUE_gt_{self.op_count['gt']})
@SP
A = M
M = -1

@END_gt_{self.op_count['gt']}
0;JMP

(FALSE_gt_{self.op_count['gt']})
@SP
A = M
M = 0

(END_gt_{self.op_count['gt']})
// SP++;
@SP
M = M + 1
'''
            self.op_count['gt'] += 1
        elif operation == "lt":
            code = f'''
// lt
@SP
M = M-1
A = M
D = M
// D becomes y

@SP
M = M-1
A = M
D = M-D

// D becomes x - y
@TRUE_lt_{self.op_count['lt']}
// Jump if x < y
D;JLT

// Jump unconditionally
@FALSE_lt_{self.op_count['lt']}
0;JMP

(TRUE_lt_{self.op_count['lt']})
@SP
A = M
M = -1

@END_lt_{self.op_count['lt']}
0;JMP

(FALSE_lt_{self.op_count['lt']})
@SP
A = M
M = 0

(END_lt_{self.op_count['lt']})
// SP++;
@SP
M = M + 1
'''
            self.op_count['lt'] += 1
        elif operation == "and":
            code = f'''
// and
@SP
M = M - 1
A = M
D = M
@SP
M = M - 1
A = M
M = D & M
@SP
M = M + 1
'''

        elif operation == "or":
            code = f'''
// or
@SP
M = M - 1
A = M
// D becomes y
D = M

@SP
M = M - 1
A = M
M = D|M
@SP
M = M + 1
'''
        elif operation == "not":
            code = f'''
// not
// neg
@SP
M = M - 1
A = M
M = !M

@SP
M = M + 1     
'''
        else:
            print("INVALID ARITHMETIC OPERATION!!!")
        # Write the code to ouput stream
        self.out_stream.write(code)


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
            elif tokens['arg1'] == 'temp':
                # push temp i
                code = f'''
// push temp {tokens['arg2']}
@{tokens['arg2']}
D = A
@5
A = D + A
D = M
@SP
A = M
M = D
@SP
M = M + 1
'''
            elif tokens['arg1'] == 'pointer':
                if tokens['arg2'] == '0':
                    # push pointer 0
                    code = f'''
// push pointer 0
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1
'''
                else:
                    # push pointer 1
                    code = f'''
// push pointer 1
@THAT
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
A = M
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
            elif tokens['arg1'] == 'temp':
                code = f'''
// pop temp {tokens['arg2']}
@{tokens['arg2']}
D = A
@5
D = D + A
@SP
A = M
M = D
@SP
M = M - 1
@SP
A = M
D = M
A = A + 1
A = M
M = D
'''
            elif tokens['arg1'] == 'pointer':
                if tokens['arg2'] == '0':
                    # pop pointer 0
                    code = f'''
// pop pointer 0
@SP
M = M - 1
A = M
D = M

@THIS 
M = D
'''
                else:
                    # pop pointer 1
                    code = f'''
// pop pointer 1
@SP
M = M - 1
A = M
D = M

@THAT 
M = D
'''
        # Write the code to ouput stream
        self.out_stream.write(code)

    # Translate label command
    def write_label(self, label):
        # Create label line with comment
        code = f"// label {label}\n({label})\n"

        # Write to the output file
        self.out_stream.write(code)

    # Translate goto command
    def write_goto(self, label):
        # Create code string for goto command
        code = f"// goto {label}\n@{label}\n0;JMP"

        # Write to the output file
        self.out_stream.write(code)

    # Translate if-goto command
    def write_if(self, label):
        # Create code string for if-goto command
        code = f'''
// if-goto label
@SP
M = M - 1
A = M
D = M

@{label}
D;JLT
'''

        # Write to the output file
        self.out_stream.write(code)

    # Close the output file stream
    def close(self):
        self.out_stream.close()
