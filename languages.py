from ProgrammingLanguage import ProgrammingLanguage

def main():
    programmingList = []
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(vb)
    programmingList.append(ruby)
    programmingList.append(python)
    programmingList.append(vb)
    print("The dynamically typed languages are:")

    for language in programmingList:
        language = str(language)
        language = language.split(",")

        name = language[0]
        typing = language[1]
        typing = typing.strip()

        language = ProgrammingLanguage(language)

        if language.is_dynamic(typing):
            print(name)
        else:
            pass



main()
