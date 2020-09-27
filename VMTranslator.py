from sys import argv
from pathlib import Path

from vparser import Parser
from code_writer import CodeWriter
from command_type import CommandType

def translate_in_file(asm_code_writer, in_file_path):
    # Construct a Parser to
    # handle input file
    vm_parser = Parser(in_file_path)

    # March through the input file,
    # parsing each line generating code from it
    while vm_parser.has_more_commands():
        vm_parser.advance()

        # Handeling push/pop commands
        if vm_parser.command_type() == CommandType.C_PUSH or vm_parser.command_type() == CommandType.C_POP:
            # Generate PUSH/POP asm Code
            asm_code_writer.write_push_pop(
                vm_parser.command_type(), vm_parser.get_tokens())

        # Handling arithmetic commands (add, sub etc.)
        elif vm_parser.command_type() == CommandType.C_ARITHMETIC:
            # Generate Arithmetic asm Code
            asm_code_writer.write_arithmetic(vm_parser.get_arg1())

        # Handling label command
        elif vm_parser.command_type() == CommandType.C_LABEL:
            # Generate Label asm Code
            asm_code_writer.write_label(vm_parser.get_arg1())

        # Handling goto command
        elif vm_parser.command_type() == CommandType.C_GOTO:
            # Generate goto asm Code
            asm_code_writer.write_goto(vm_parser.get_arg1())

        # Handling if-goto command
        elif vm_parser.command_type() == CommandType.C_IF:
            # Generate if-goto asm Code
            asm_code_writer.write_if(vm_parser.get_arg1())

        elif vm_parser.command_type() == CommandType.C_FUNCTION:
            # Generate function asm Code
            asm_code_writer.write_function(
                vm_parser.get_arg1(), vm_parser.get_arg2())

        elif vm_parser.command_type() == CommandType.C_CALL:
            # Generate call asm code
            asm_code_writer.write_call(vm_parser.get_arg1(), vm_parser.get_arg2())

        elif vm_parser.command_type() == CommandType.C_RETURN:
            # Generate return asm code
            asm_code_writer.write_return()


def main():
    # Input file Path
    in_file = Path(argv[1])

    # Check if provided argument is
    # a file or a directory
    if (in_file.is_dir()):
        # Argument path to a directory
        out_file = in_file / in_file.with_suffix(".asm")

    elif (in_file.is_file()):
        # Argument is path to a file
        # Output file Path
        out_file = in_file.with_suffix(".asm")
    
    # Construct a CodeWriter to
    # handle output file
    asm_writer = CodeWriter(out_file)

    if (in_file.is_file()):
        # Translate the single file
        translate_in_file(asm_writer, in_file)

    elif (in_file.is_dir()):
        # Have to loop through every file
        asm_writer.write_bootstrap_code()

        # Loop through each file and translate
        for f in in_file.iterdir():
            # File is .vm file?
            if f.suffix == ".vm":
                print(f"translating {f.name}...")
                asm_writer.set_file_name(f.stem)
                translate_in_file(asm_writer, f)


    

if __name__ == '__main__':
    main()
