from sys import argv
from pathlib import Path

from vparser import Parser
from code_writer import CodeWriter
from command_type import CommandType

def main():
    # Input file Path
    in_file = Path(argv[1])

    #Output file Path
    out_file = in_file.with_suffix(".asm")

    # Construct a Parser to 
    # handle input file
    vm_parser = Parser(in_file)

    # Construct a CodeWriter to 
    # handle output file
    asm_writer = CodeWriter(out_file)

    # March through the input file,
    # parsing each line generating code from it
    while vm_parser.has_more_commands():
        vm_parser.advance()
        
        if vm_parser.command_type() == CommandType.C_PUSH or vm_parser.command_type() == CommandType.C_POP:
            # Generate PUSH/POP asm Code
            asm_writer.write_push_pop(vm_parser.command_type(), vm_parser.get_tokens())

        elif vm_parser.command_type() == CommandType.C_ARITHMETIC:
            # Generate Arithmetic asm Code
            asm_writer.write_arithmetic(vm_parser.get_arg1())
if __name__ == '__main__':
    main()