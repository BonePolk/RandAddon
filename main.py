from random import *
from parser import *
from time import sleep

while True:
	while True:
	   try:
	       page = randint(1,parserpages("mods"))
	       print("Страница N°", page, sep="")
	       print(*parser(randint(0,9), page, "mods"), sep = "")
	       print("следующий введите Enter")
	       input()
	       break
	   except Exception as ex:
	       print(ex)