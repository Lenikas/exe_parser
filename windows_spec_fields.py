import struct


class WindowsSpecificFieldsParser:
    """Парсим поля заголовка WINDOWS SPECIFIC FIELDS"""

    @staticmethod
    def parse_image_base(data, offset):
        base = struct.unpack("<i", data[offset + 52: offset + 56])[0]
        base_hex = data[offset + 52: offset + 56].hex()
        return base_hex

    @staticmethod
    def parse_section_alignment(data, offset):
        section = struct.unpack("<i", data[offset + 56: offset + 60])[0]
        section_hex = data[offset + 56: offset + 60].hex()
        return section_hex

    @staticmethod
    def parse_file_alignment(data, offset):
        f_alignment = struct.unpack("<i", data[offset + 60: offset + 64])[0]
        f_alignment_hex = data[offset + 60: offset + 64].hex()
        return f_alignment_hex

    @staticmethod
    def parse_major_version_op(data, offset):
        version_op = struct.unpack("<h", data[offset + 64: offset + 66])[0]
        return version_op

    @staticmethod
    def parse_minor_version_op(data, offset):
        version_op = struct.unpack("<h", data[offset + 66: offset + 68])[0]
        return version_op

    @staticmethod
    def parse_major_version_image(data, offset):
        version_image = struct.unpack("<h", data[offset + 68: offset + 70])[0]
        return version_image

    @staticmethod
    def parse_minor_version_image(data, offset):
        version_image = struct.unpack("<h", data[offset + 70: offset + 72])[0]
        return version_image

    @staticmethod
    def parse_major_subsystem_version(data, offset):
        version_subsystem = struct.unpack("<h", data[offset + 72: offset + 74])[0]
        return version_subsystem

    @staticmethod
    def parse_minor_subsystem_version(data, offset):
        version_subsystem = struct.unpack("<h", data[offset + 74: offset + 76])[0]
        return version_subsystem

    @staticmethod
    def parse_win32_version_value(data, offset):
        version = struct.unpack("<i", data[offset + 76: offset + 80])[0]
        return version

    @staticmethod
    def parse_size_image(data, offset):
        size = struct.unpack("<i", data[offset + 80: offset + 84])[0]
        return size

    @staticmethod
    def parse_size_headers(data, offset):
        size = struct.unpack("<i", data[offset + 84: offset + 88])[0]
        return size

    @staticmethod
    def parse_check_sum(data, offset):
        check_sum = struct.unpack("<i", data[offset + 88: offset + 92])[0]
        return check_sum

    @staticmethod
    def prepare_subsystem():
        return {
            0: ("IMAGE_SUBSYSTEM_UNKNOWN", "Unknown subsystem"),
            1: ("IMAGE_SUBSYSTEM_NATIVE", "No subsystem required (device drivers and native system processes)"),
            2: ("IMAGE_SUBSYSTEM_WINDOWS_GUI", "Windows graphical user interface (GUI) subsystem"),
            3: ("IMAGE_SUBSYSTEM_WINDOWS_CUI", "Windows character-mode user interface (CUI) subsystem"),
            5: ("IMAGE_SUBSYSTEM_OS2_CUI", "OS/2 CUI subsystem"),
            7: ("IMAGE_SUBSYSTEM_POSIX_CUI", "POSIX CUI subsystem"),
            9: ("IMAGE_SUBSYSTEM_WINDOWS_CE_GUI", "Windows CE system"),
            10: ("IMAGE_SUBSYSTEM_EFI_APPLICATION", "Extensible Firmware Interface (EFI) application"),
            11: ("IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER", "EFI driver with boot services"),
            12: ("IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER", "EFI driver with run-time services"),
            13: ("IMAGE_SUBSYSTEM_EFI_ROM", "EFI ROM image"),
            14: ("IMAGE_SUBSYSTEM_XBOX", "Xbox system"),
            16: ("IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION", "Boot application"),
        }

    @staticmethod
    def parse_subsystem(data, offset):
        dict_subsystem = WindowsSpecificFieldsParser.prepare_subsystem()
        subsystem = struct.unpack("<h", data[offset + 92: offset + 94])[0]
        return dict_subsystem[subsystem]

    @staticmethod
    def prepare_dll_characteristic():
        pass

    @staticmethod
    def parse_dll_characteristic(data, offset):
        pass

    @staticmethod
    def parse_size_of_stack_reserve(data, offset):
        size = struct.unpack("<i", data[offset + 96: offset + 100])[0]
        return size

    @staticmethod
    def parse_size_of_stack_commit(data, offset):
        size = struct.unpack("<i", data[offset + 100: offset + 104])[0]
        return size

    @staticmethod
    def parse_size_of_heap_reserve(data, offset):
        size = struct.unpack("<i", data[offset + 104: offset + 108])[0]
        return size

    @staticmethod
    def parse_size_of_heap_commit(data, offset):
        size = struct.unpack("<i", data[offset + 108: offset + 112])[0]
        return size

    @staticmethod
    def parse_loader_flags(data, offset):
        flags = struct.unpack("<i", data[offset + 112: offset + 116])[0]
        return flags

    @staticmethod
    def parse_number_rva_and_sizes(data, offset):
        number = struct.unpack("<i", data[offset + 116: offset + 120])[0]
        return number

    @staticmethod
    def create_result(data, offset):
        print("Windows Specific Fields")
        print("ImageBase - {0}".format(WindowsSpecificFieldsParser.parse_image_base(data, offset)))
        print("SectionAlignment - {0}".format(WindowsSpecificFieldsParser.parse_section_alignment(data, offset)))
        print("FileAlignment - {0}".format(WindowsSpecificFieldsParser.parse_file_alignment(data, offset)))
        print("MajorOperatingSystemVersion - {0}".format(
            WindowsSpecificFieldsParser.parse_major_version_op(data, offset)))
        print("MinorOperatingSystemVersion - {0}".format(
            WindowsSpecificFieldsParser.parse_minor_version_op(data, offset)))
        print("MajorImageVersion - {0}".format(
            WindowsSpecificFieldsParser.parse_major_version_image(data, offset)))
        print("MinorImageVersion - {0}".format(
            WindowsSpecificFieldsParser.parse_minor_version_image(data, offset)))
        print("MajorSubsystemVersion - {0}".format(
            WindowsSpecificFieldsParser.parse_major_subsystem_version(data, offset)))
        print("MinorSubsystemVersion - {0}".format(
            WindowsSpecificFieldsParser.parse_minor_subsystem_version(data, offset)))
        print("Win32VersionValue - {0}".format(WindowsSpecificFieldsParser.parse_win32_version_value(data, offset)))
        print("SizeOfImage - {0}".format(WindowsSpecificFieldsParser.parse_size_image(data, offset)))
        print("SizeOfHeaders - {0}".format(WindowsSpecificFieldsParser.parse_size_headers(data, offset)))
        print("CheckSum - {0}".format(WindowsSpecificFieldsParser.parse_check_sum(data, offset)))
        print("Subsystem - {0}".format(WindowsSpecificFieldsParser.parse_subsystem(data, offset)))
        print("SizeOfStackReserve - {0}".format(WindowsSpecificFieldsParser.parse_size_of_stack_reserve(data, offset)))
        print("SizeOfStackCommit - {0}".format(WindowsSpecificFieldsParser.parse_size_of_stack_commit(data, offset)))
        print("SizeOfHeapReserve - {0}".format(WindowsSpecificFieldsParser.parse_size_of_heap_reserve(data, offset)))
        print("SizeOfHeapCommit - {0}".format(WindowsSpecificFieldsParser.parse_size_of_heap_commit(data, offset)))
        print("LoaderFlags - {0}".format(WindowsSpecificFieldsParser.parse_loader_flags(data, offset)))
        print("NumberOfRvaAndSizes - {0}".format(WindowsSpecificFieldsParser.parse_number_rva_and_sizes(data, offset)))