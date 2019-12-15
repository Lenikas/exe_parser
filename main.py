from dos_header import DosHeaderParser


def main():
    with open(r"C:\Users\Леня\Desktop\lenika\Windscribe\Windscribe.exe", "rb") as file:
        data = file.read()
        print(DosHeaderParser.parse_e_magic(data))
        print(DosHeaderParser.parse_e_lfanew(data))



if __name__== '__main__':
    main()