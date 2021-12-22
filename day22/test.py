import pytest

from day22.main import Reactor


@pytest.mark.parametrize(
    "command, expected",
    [
        ("on x=10..12,y=10..12,z=10..12", 27),
    ],
)
def test_commands(command, expected):
    reactor = Reactor()
    reactor.execute_reboot_command(command)

    assert reactor.number_on() == expected
