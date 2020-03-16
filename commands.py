"""
IPAssign command definitions.
"""
from enum import Enum


class commands(Enum):
    REQUEST_PARAMS = 0x0002
    SEND_PARAMS = 0x0003

    RESET = 0x0004
    RESET_ACK = 0x0005

    CHANGE_IP = 0x0006
    CHANGE_IP_ACK = 0x0007

    SEND_RAW_DATA = 0x0008

    SEND_FIRMWARE_DATA = 0x000A
    WRITE_FIRMWARE = 0x000C

    SEND_ASC_DATA = 0x000E

    CHANGE_PARAMS = 0x000F
    CHANGE_PARAMS_ACK = 0x0010