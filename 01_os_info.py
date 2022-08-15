#-*- coding: utf-8 -*-

# Нужно собрать информацию об операционной системе и версии пайтона

# TODOO запустить этот скрипт и закоммитить результат его работы (файл os_info.txt)
import platform
import sys



info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('01_os_info.txt', 'w') as ff:
    ff.write(info)
