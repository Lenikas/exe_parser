import struct


class DosHeaderParser:

    @staticmethod
    def parse_e_magic(data):
        e_magic = data[0:2]
        return e_magic

    @staticmethod
    def parse_e_lfanew(data):
        e_lfanew = struct.unpack_from("<H", data[60:62])
        return  e_lfanew