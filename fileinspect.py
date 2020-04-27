import os
import json
import argparse
import shutil

SIGNATURE_TABLE = 'config/signature.json'


parser = argparse.ArgumentParser(description="Check file")
parser.add_argument('-f', '--file', action='store', type=str,
                    help='input path to file')
parser.add_argument('-d', '--dir', action='store',
                    type=str, help='input path to file')
parser.add_argument('-o', '--output', action='store', type=str,
                    help='output directory for saving file with extension')


def binary_inspection(file: str) -> str:
    '''
    Read file bytes and check it`s signatures in signatures tables.
    '''
    result = " "
    with open(SIGNATURE_TABLE, 'r') as signature_table:
        extension_dict = json.load(signature_table)
    with open(file, 'rb') as file_obj:
        file_heading = file_obj.read(extension_dict.get(32))
    hex_bytes = ' '.join(['{:02X}'.format(_byte)
                          for _byte in file_heading])
    for extension in extension_dict:
        current_size = extension_dict.get(extension).get('size')
        current_signature = extension_dict.get(extension).get('signature')
        if hex_bytes[:current_size * 2 + current_size - 1] in current_signature:
            result = extension
            break
        else:
            result = "Not found"
    return result


def directory_inspection(directory: str,  output_directory=""):
    files = os.listdir(directory)
    if output_directory:
        for file in files:
            extension = binary_inspection(directory + '\\' + file)
            if extension != "Not found":
                shutil.copyfile(directory + '\\' + file,
                                output_directory + '\\' + file + f'.{extension}')
    else:
        for file in files:
            extension = binary_inspection(directory + '\\' + file)
            print(f'{file} - extension:{extension}')


if __name__ == "__main__":
    args = parser.parse_args()
    if args.file:
        print(binary_inspection(args.file))
    elif args.dir:
        if args.output:
            directory_inspection(args.dir,  args.output)
        else:
            directory_inspection(args.dir)
