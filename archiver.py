import os
import hashlib
from shannon_fano import *
from window import start_window


def main_command(args):
    if os.path.isfile(args.input):
        do_action(args.compress, args.input)
    elif os.path.isdir(args.input):
        for address, dirs, files in os.walk(args.input):
            for file in files:
                if args.compress or file.split('.')[-1] == 'sf':
                    do_action(args.compress, os.path.join(address, file))
    else:
        print("Input file not exist")


def do_action(is_compress, filename, is_checksum=True):
    if is_compress:
        filename_out = filename.rsplit('.', 1)[0] + '.sf'
        print(f'Compress from {filename} to {filename_out}')
        d, bc, occurrence = count_bytes(filename)
        information_gain, input_entropy = entropy(d)
        code_len = calculate_code_len(d)
        code = create_code(code_len)
        compress(filename, code, calculate_padding(code_len, occurrence), filename_out)
        if is_checksum:
            with open(filename_out+'.md5', 'w') as hash_file:
                hash_file.write(hashlib.md5(open(filename_out, 'rb').read()).hexdigest())
            print("Generated hash " + filename_out+'.md5')
    else:
        if is_checksum:
            md_hash = open(filename + '.md5').read()
            cur_hash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
            if md_hash != cur_hash:
                print("File corrupted!", filename)
                return
        filename_out = filename.rsplit('.', 1)[0] + '.un'
        print(f'Extract from {filename} to {filename_out}')
        extract(filename, filename_out)



if __name__ == '__main__':
    start_window(main_command)
