import sys

from dos_header import DosHeaderParser
from coff_header import CoffHeaderParser
from standart_coff_fields import StandartCoffFieldsParser
from windows_spec_fields import WindowsSpecificFieldsParser
import argparse


def prepare_arguments():
    parser = argparse.ArgumentParser(description="Parser for headers")
    parser.add_argument('-dos', help=str(DosHeaderParser.__doc__), nargs=1)
    parser.add_argument('-coff', help=str(CoffHeaderParser.__doc__), nargs=1)
    parser.add_argument('-standart_coff', help=str(StandartCoffFieldsParser.__doc__), nargs=1)
    parser.add_argument('-windows_spec', help=str(WindowsSpecificFieldsParser.__doc__), nargs=1)
    parser.add_argument('-all_headers', nargs=1)
    return parser.parse_args()


def print_all_headers(data, offset):
    DosHeaderParser.create_result(data)
    print("")
    CoffHeaderParser.create_result(data, offset)
    print("")
    StandartCoffFieldsParser.create_result(data, offset)
    print("")
    WindowsSpecificFieldsParser.create_result(data, offset)


def main():
    args = prepare_arguments()
    file = sys.argv[2]
    with open(file, "rb") as file:
        data = file.read()
        offset = DosHeaderParser.parse_e_lfanew(data)
    if args.dos:
        DosHeaderParser.create_result(data)
    elif args.coff:
        CoffHeaderParser.create_result(data, offset)
    elif args.standart_coff:
        StandartCoffFieldsParser.create_result(data, offset)
    elif args.windows_spec:
        WindowsSpecificFieldsParser.create_result(data, offset)
    elif args.all_headers:
        print_all_headers(data, offset)
    else:
        raise SyntaxError


if __name__ == '__main__':
    main()