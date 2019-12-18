import struct
import datetime


class CoffHeaderParser:
    """Парсим поля заголовка COFF"""

    @staticmethod
    def parse_signature(data, offset):
        """Проверяем, что файл соответствует исполняемому"""
        signature = data[offset: offset + 2]
        return signature

    @staticmethod
    def parse_machine(data, offset):
        """Парсим архитектуру процессора,на которой данной приложение может исполняться"""
        machine = struct.unpack("<H", data[offset+4: offset+6])[0]
        if machine == 332:
            return "x86"
        return data[offset+5: offset+6]

    @staticmethod
    def parse_section(data, offset):
        """Парсим количество секций в файле"""
        number_section = struct.unpack_from("<H", data[offset + 6:offset + 8])[0]
        return number_section

    @staticmethod
    def parse_time_data_stamp(data, offset):
        """Парсим дату и время создания файла"""
        time_data = struct.unpack("<I", data[offset + 8:offset + 12])[0]
        date_time_iso = datetime.datetime.fromtimestamp(time_data).isoformat()
        return date_time_iso

    @staticmethod
    def parse_pointer_to_symbol_table(data, offset):
        """Парсим смещение до таблицы символов"""
        pointer = struct.unpack("<i", data[offset + 12:offset + 16])[0]
        return pointer

    @staticmethod
    def parse_number_of_symbols(data, offset):
        """"""
        number = struct.unpack("<i", data[offset + 16:offset + 20])[0]
        return number

    @staticmethod
    def parse_size_optional_header(data, offset):
        """Парсим размер опционального заголовка"""
        size = struct.unpack("<H", data[offset + 20:offset + 22])[0]
        return size

    @staticmethod
    def prepare_characteristics():
        """Подготавливаем словарь с характеристиками и их значениями"""
        return {
            "0": ("IMAGE_FILE_RELOCS_STRIPPED", "Relocation information was stripped from file"),
            "1": ("IMAGE_FILE_EXECUTABLE_IMAGE", "The file is executable"),
            "2": ("IMAGE_FILE_LINE_NUMS_STRIPPED", "COFF line numbers were stripped from file"),
            "3": ("IMAGE_FILE_LOCAL_SYMS_STRIPPED", "COFF symbol table entries were stripped from file"),
            "4": ("IMAGE_FILE_AGGRESIVE_WS_TRIM", "Aggressively trim the working set(obsolete)"),
            "5": ("IMAGE_FILE_LARGE_ADDRESS_AWARE", "The application can handle addresses greater than 2 GB"),
            "6": ("", ""),
            "7": ("IMAGE_FILE_BYTES_REVERSED_LO", "The bytes of the word are reversed(obsolete)"),
            "8": ("IMAGE_FILE_32BIT_MACHINE", "The computer supports 32-bit words"),
            "9": ("IMAGE_FILE_DEBUG_STRIPPED", "Debugging information was removed and stored separately in another file"),
            "10": ("IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP", "If the image is on removable media, copy it to and run it from the swap file"),
            "11": ("IMAGE_FILE_NET_RUN_FROM_SWAP", "If the image is on the network, copy it to and run it from the swap file"),
            "12": ("IMAGE_FILE_SYSTEM", "The image is a system file"),
            "13": ("IMAGE_FILE_DLL", "The image is a DLL file"),
            "14": ("IMAGE_FILE_UP_SYSTEM_ONLY", "The image should only be ran on a single processor computer"),
            "15": ("IMAGE_FILE_BYTES_REVERSED_HI", "The bytes of the word are reversed(obsolete)"),
        }

    @staticmethod
    def parse_characteristics(data, offset):
        """Проверяем, какие характеристики присутсвуют в соответствующем поле"""
        list_charact = []
        dict_charact = CoffHeaderParser.prepare_characteristics()
        number_charact = 0
        for b in data[offset + 22:offset + 24]:
            for i in range(8):
                bit = (b >> i) & 1
                if bit == 1:
                    list_charact.append(dict_charact[str(number_charact)])
                number_charact += 1
        return list_charact

    @staticmethod
    def create_result(data, offset):
        print("PE HEADER")
        print("Signature - {0}".format(CoffHeaderParser.parse_signature(data, offset)))
        print("COFF HEADER (part of PE)")
        print("Machine - {0}".format(CoffHeaderParser.parse_machine(data, offset)))
        print("Number of section - {0}".format(CoffHeaderParser.parse_section(data, offset)))
        print("TimeDataStamp - {0}".format(CoffHeaderParser.parse_time_data_stamp(data, offset)))
        print("PointerToSymbolTable - {0}".format(CoffHeaderParser.parse_pointer_to_symbol_table(data, offset)))
        print("NumberOfSymbols - {0}".format(CoffHeaderParser.parse_number_of_symbols(data, offset)))
        print("SizeOfOptionalHeader - {0}".format(CoffHeaderParser.parse_size_optional_header(data, offset)))
        print("Characteristics - {0}".format(CoffHeaderParser.parse_characteristics(data, offset)))