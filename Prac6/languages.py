# import ProgrammingLanguage from programming_language.py
from Prac6.programming_language import ProgrammingLanguage


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

program_list = [ruby, python, visual_basic]
print("The dynamically typed languages are \n",)
for i in program_list:
    if i.is_dynamic():
        print(i.name)