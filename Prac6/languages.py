# import ProgrammingLanguage from programming_language.py
from Prac6.programming_language import ProgrammingLanguage


def main():
    """ start of program """
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are \n", )
    for i in languages:
        if i.is_dynamic():
            print(i.name)


if __name__ == "__main__":
    main()
