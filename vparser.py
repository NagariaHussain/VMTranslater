# The command type Enum
from command_type import CommandType


class Parser:
    '''Parses each VM command into its lexical elements'''

    # Opens the input file/stream and
    # gets ready to parse it
    def __init__(self, in_path):
        # Open file sream
        self.in_stream = in_path.open("r")

    # Are there more commands in input?
    def has_more_commands(self):
        # Read a line from the input stream
        line = self.in_stream.readline()

        # If the line is non-empty
        if line:
            # Clean the line
            line = line.strip(" ").rstrip("\n")

            # Check for comments
            if line.startswith("//"):
                # Ignore this line and look for more commands
                # Recursive call
                return self.has_more_commands()

            # Set this to the current command
            self.current_line = line
            return True

        # Nothing left to read
        return False

    # Reads the next command from the input
    # and makes it the current command
    def advance(self):
        # Update current command
        self.current_command = self.current_line
        # Tokenize the current command
        self.tokenize()

    # Returns a constant representing
    # a command type
    def command_type(self):
        # Number of tokens is 1: op_type
        if len(self.tokens) == 1:
            # Command is return
            if self.get_arg1() == 'return':
                return CommandType.C_RETURN
            # Command is arithmetic type
            return CommandType.C_ARITHMETIC

        # Number of tokens is 2: op_type arg1
        elif len(self.tokens) == 2:
            # Is label command
            if self.tokens['op_type'] == 'label':
                return CommandType.C_LABEL

            # Is goto command
            elif self.tokens['op_type'] == 'goto':
                return CommandType.C_GOTO

            # Is if-goto command
            elif self.tokens['op_type'] == 'if-goto':
                return CommandType.C_IF

        # Number of tokens is 3: op_type arg1 arg2
        elif len(self.tokens) == 3:
            # Is a push command
            if self.tokens['op_type'] == 'push':
                return CommandType.C_PUSH

            # Is a pop command
            elif self.tokens['op_type'] == 'pop':
                return CommandType.C_POP

            # Is a function funcName nLocals command
            elif self.tokens['op_type'] == 'function':
                return CommandType.C_FUNCTION

            # Is a call funcName nArgs command
            elif self.tokens['op_type'] == 'call':
                return CommandType.C_CALL

    # get arg1
    def get_arg1(self):
        return self.tokens['arg1']

    # get arg2
    def get_arg2(self):
        return self.tokens['arg2']

    # tokenize the input lines
    def tokenize(self):
        self.tokens = {}

        # Split on white space
        tokens = self.current_command.split()

        if len(tokens) == 1:
            # arithmetic/return operation
            self.tokens['arg1'] = tokens[0]

        elif len(tokens) == 2:
            self.tokens['op_type'] = tokens[0]
            self.tokens['arg1'] = tokens[1]

        elif len(tokens) == 3:
            # segment
            self.tokens['arg1'] = tokens[1]
            # index
            self.tokens['arg2'] = tokens[2]
            # operation
            self.tokens['op_type'] = tokens[0]

    # get tokens
    def get_tokens(self):
        return self.tokens
