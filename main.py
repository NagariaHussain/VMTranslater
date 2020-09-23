from sys import argv
from pathlib import Path

from parser import Parser
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


if __name__ == '__main__':
    main()