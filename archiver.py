from shannon_fano import *
from window import start_window


def main_command(args):
    if args.compress:
        filename_out = args.input + '.sf'
        if args.output:
            filename_out = args.output
        print(f'Compress from {args.input} to {filename_out}')
        d, bc, occurrence = count_bytes(args.input)
        information_gain, input_entropy = entropy(d)
        code_len = calculate_code_len(d)
        code = create_code(code_len)
        compress(args.input, code, calculate_padding(code_len, occurrence), filename_out)
        exit(0)
    else:
        filename_out = args.input + '.un'
        if args.output:
            filename_out = args.output
        print(f'Extract from {args.input} to {filename_out}')
        extract(args.input, filename_out)
        exit(0)


if __name__ == '__main__':
    start_window(main_command)
