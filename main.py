from random import randint

from parser import parser

def main():
    while True:
        while True:
            try:
                page = randint(1, parser.parserpages("mods"))
                print("Страница N°", page, sep="")
                print(*parser.parser(randint(0, 9), page, "mods"), sep="")
                print("Следующий введите Enter")
                input()
                break
            except Exception as ex:
                print(ex)

def test():
    parser.download(3349, "test.mcpack")

if __name__ == "__main__":
    test()
