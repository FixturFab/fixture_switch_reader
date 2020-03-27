"""
fixture_io.py

Contains FixtureSwitch class for reading fixture switch states from the
Fixture Switch Reader.
"""

import serial


class FixtureSwitch(object):
    def __init__(self, com_port):
        """
        Connect to the FixtureSwitch device using the provided COM port

        :param com_port: COM Port for the Fixture Switch
        :type com_port: str
        """
        self.ser = serial.Serial(com_port, 115200)

    def get_info(self):
        """
        Read information about the connected device

        Return a dictionary containing the following information from the
        device:

        - Company
        - Device
        - Firmware Version

        :return: Device info dictionary
        :rtype: dict
        """
        self.ser.write(b"version")
        company = self.ser.readline().strip().decode("utf-8")
        device = self.ser.readline().strip().decode("utf-8")
        fw_ver = self.ser.readline().strip().decode("utf-8")

        return {
            'company': company,
            'device': device,
            'fw_ver': int(fw_ver.split(":")[-1])
        }

    def read_switch(self):
        """
        Read the current state of the fixture switch

        :return: Fixture state, True if closed, False if open
        :rtype: bool
        """
        self.ser.write(b"read_switch")
        return bool(int(self.ser.readline().strip().decode("utf-8")))
