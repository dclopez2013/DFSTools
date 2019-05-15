from datetime import datetime
from ctypes import *
import os, sys
from gooey import Gooey
from gooey import GooeyParser

kernel32 = windll.kernel32

@Gooey(optional_cols=1, program_name="Python File Attribute Parser")
def main():
    desc = "Select file to parse for file attributes"
    parser = GooeyParser(description=desc, add_help=False)
    parser.add_argument("--filename", default="", widget='FileChooser')
    parser.add_argument("--dirchooser", default="", widget='DirChooser')
    args = parser.parse_args()

    file = args.filename
    dir = args.dirchooser

    if not file and not dir:
        print("No files selected")
    if dir and not file:
        scanDir(dir)
    elif file and not dir:
        scanFile(file)

    with os.scandir(dir) as dir_contents:
        for entry in dir_contents:
            info = entry.stat()
            print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
            print(f'{entry.name}\t Item Size: {info.st_size} bytes')
            print(f'{entry.name}\t Last Accessed: {convert_date(info.st_atime)}')
            print(f'{entry.name}\t Creation Time: {convert_date(info.st_ctime)}')
            print(f'{entry.name}\t Group ID of Owner: {info.st_gid}')
            print(f'{entry.name}\t Use ID of Owner: {info.st_uid}')




def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def scanFile(file):
    print(str(file))

def scanDir(dir):
    print(str(dir))


if __name__ == '__main__':
    main()