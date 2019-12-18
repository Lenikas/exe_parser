import struct


class StandartCoffFieldsParser:
    """Парсим поля заголовка STANDART COFF FIELDS"""

    @staticmethod
    def parse_magic(data, offset):
        """Парсим сигнатуру"""
        magic = struct.unpack("<H", data[24 + offset:26 + offset])[0]
        if magic == 267:
            return "32 bit"
        elif magic == 523:
            return "64 bit"
        else:
            return "ROM image"

    @staticmethod
    def parse_major_linker_version(data, offset):
        """Парсим версию линкера, создавшего файл"""
        major_version = struct.unpack("<b", data[offset + 26: offset + 27])[0]
        return major_version

    @staticmethod
    def parse_minor_linker_version(data, offset):
        minor_version = struct.unpack("<b", data[offset + 27: offset + 28])[0]
        return minor_version

    @staticmethod
    def parse_size_of_code(data, offset):
        """Парсим раздел размера кода или сумму нескольких, если они есть"""
        size = struct.unpack("<i", data[offset + 28: offset + 32])[0]
        return size

    @staticmethod
    def parse_size_of_initialized_data(data, offset):
        """Парсим размер секции инициализированных данных, или сумму нескольких, если они есть"""
        size = struct.unpack("<i", data[offset + 32: offset + 36])[0]
        return size

    @staticmethod
    def parse_size_of_uninitialized_data(data, offset):
        """Парсим размер секции неинициализированных данных, или сумму нескольких, если они есть"""
        size = struct.unpack("<i", data[offset + 36: offset + 40])[0]
        return size

    @staticmethod
    def parse_address_entry_point(data, offset):
        """Парсим RVA адрес точки входа в программу, те место, скоторого программа выполняется"""
        pass

    @staticmethod
    def parse_base_of_code(data, offset):
        """Парсим RVA адрес начала секции кода"""
        pass

    @staticmethod
    def parse_base_of_data(data, offset):
        """Парсим RVA дрес начала секции данных"""
        pass

    @staticmethod
    def create_result(data, offset):
        print("StandartCoffFields")
        print("Magic signature - {0}".format(StandartCoffFieldsParser.parse_magic(data, offset)))
        print("MajorLinkerVersion - {0}".format(StandartCoffFieldsParser.parse_major_linker_version(data, offset)))
        print("MinorLinkerVersion - {0}".format(StandartCoffFieldsParser.parse_minor_linker_version(data, offset)))
        print("SizeOfCode - {0}".format(StandartCoffFieldsParser.parse_size_of_code(data, offset)))
        print("SizeOfInitializedData - {0}".format(StandartCoffFieldsParser.parse_size_of_initialized_data(data, offset)))
        print("SizeOfUninitializedData - {0}".format(StandartCoffFieldsParser.parse_size_of_uninitialized_data(data, offset)))