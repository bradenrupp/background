import ctypes
import os

pathToBmp = os.path.normpath("/c/Windows/Web/Wallpaper/Windows/img0.jpg")
print(pathToBmp)
SPI_SETDESKTOPWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, pathToBmp, 0)