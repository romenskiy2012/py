'''
Библиотека Essentials

Copyright © Upbits, 2017 – 2018.
GitHub: http://github.com/Upbits/Essentials

Последнее изменение сделал Ketsu8, (2017 года, 6 декабря).
'''
import platform
import os
import zipfile
from colorama import Fore, Style

def unZip(fromZip, toPath): #самописная функция для разархивирования zip акривов которая делает из 2 строчек одну
	with zipfile.ZipFile(fromZip, "r") as zip_ref:
                    zip_ref.extractall(toPath)

def universalClear(): #самописная функция для универсальной отчистки экрана
	if platform.system() == "Windows": #если платформа Windows
		os.system("cls") #то пишется cls
	else: #если нет
		os.system("clear") #то просто clear

def colorText(text, color): #функция для отображения кастомного текста в терминале
    if color == "red":
        return Fore.RED + text + Style.RESET_ALL
    elif color == "yellow":
        return Fore.YELLOW + text + Style.RESET_ALL
    elif color == "green":
        return Fore.GREEN + text + Style.RESET_ALL
    elif color == "blue":
        return Fore.BLUE     + text + Style.RESET_ALL
    elif color == "magenta":
        return Fore.MAGENTA + text + Style.RESET_ALL
    elif color == "cyan":
        return Fore.CYAN + text + Style.RESET_ALL

def textFromFile(file): #функция для получения текста из файла
	return open(file, "r").read()

def textToFile(file, text): #функция что-бы записывать текст в файл
	filea = open(file,"w+")
	filea.write(text)
	filea.close()
