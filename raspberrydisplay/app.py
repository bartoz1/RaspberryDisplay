from raspberrydisplay.internet_connection import check_internet
from raspberrydisplay.display import init


def run():
    init()
    check_internet()