import pytest

from fixture_io import FixtureSwitch


fixture_sw = FixtureSwitch("/dev/ttyACM0")


def test_get_version():
    info = fixture_sw.get_info()

    assert info['company'] == "FixturFab Inc.", "incorrect company name"
    assert info['device'] == "Fixture Switch Reader", "incorrect device name"
    assert info['fw_ver'] == 1, "incorrect firmware version"


def test_read_switch():
    assert not fixture_sw.read_switch(), "incorrect fixture switch state"
