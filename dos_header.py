import struct


class DosHeaderParser:
    """Парсим нужные поля из DOS заголовка"""

    @staticmethod
    def parse_e_magic(data):
        """Проверяем наличие магической сигнатуры"""
        e_magic = str(data[0:2])
        return e_magic

    @staticmethod
    def parse_e_lfanew(data):
        """Находим смещение, по которому находится начало PE заголовка"""
        e_lfanew = struct.unpack_from("<H", data[60:62])[0]
        return e_lfanew

    @staticmethod
    def create_result(data):
        print("DOS HEADER")
        print("e_magic - {0}".format(DosHeaderParser.parse_e_magic(data)))
        print("e_lfanew - {0}".format(DosHeaderParser.parse_e_lfanew(data)))