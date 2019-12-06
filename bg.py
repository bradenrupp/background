#!/usr/bin/env python3

import ctypes
import os
import time


def change_bg():
    pathToBmp = os.path.normpath("C:/Users/Public/.bg.bmp")
    print(pathToBmp)
    SPI_SETDESKTOPWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKTOPWALLPAPER, 0, pathToBmp, 0)


if __name__ == '__main__':
    while True:
        time.sleep(5)
        change_bg()
        time.sleep(5)
