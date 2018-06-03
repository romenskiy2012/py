import os, platform

class clear():
    def __init__(self): #самописная функция для универсальной отчистки экрана
	    if platform.system() == "Windows": #если платформа Windows
		    os.system("cls") #то пишется cls
	    else: #если нет
		    os.system("clear") #то просто clear