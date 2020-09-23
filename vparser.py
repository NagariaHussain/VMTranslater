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
        # TODO: consider comments and empty lines
        
        # Read a line from the input stream
        line = self.in_stream.readline()

        # If the line is non-empty
        if line:
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
        if len(self.tokens) == 1:
            return CommandType.C_ARITHMETIC
        elif len(self.tokens) == 3:
            if self.tokens['op_type'] == 'push':
                return CommandType.C_PUSH
            elif self.tokens['op_type'] == 'pop':
                return CommandType.C_POP

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
            # arithmetic operation
            self.tokens['arg1'] = tokens[0]
        elif len(tokens) == 3:
            # segment
            self.tokens['arg1'] = tokens[1]
            # index
            self.tokens['arg2'] = tokens[2]
            # push/pop
            self.tokens['op_type'] = tokens[0]

    # get tokens
    def get_tokens(self):
        return self.tokens