import argparse
from shannon_fano import *
import tkinter

s = tkinter.Tk()
s.mainloop()
parser = argparse.ArgumentParser(description='Archiver on Shannon-Fano compression algorithm.')
parser.add_argument('--compress', '-c', action='store_true', default=False, help='Compress file')
parser.add_argument('--extract', '-e', action='store_true', default=False, help='Extract file')
parser.add_argument('--input', '-i', action='store', default='', help='File to compress or extract', required=True)
parser.add_argument('--output', '-o', action='store', default='', help='File to save result', required=False)

args = parser.parse_args()

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


if args.extract:
    filename_out = args.input + '.un'
    if args.output:
        filename_out = args.output
    print(f'Extract from {args.input} to {filename_out}')
    extract(args.input, filename_out)
    exit(0)

print('No function: -c --compress, -e --extract')
