import json


def takeIn():
    ara = input(": ").replace("\n", "")
    return ara


def startUp():
    print("booting up all stuff")
    # with open()


def saveAndClose():
    print("saved successfully !")


def options():
    print("""available options are 
                                    1 - add a reminder
                                    2 - check all reminders
                                    e - exit""")


def addReminder(whatToDo):  # opton 1
    if whatToDo == "bad data in input and cant process it":
        return True


startUp()
bigEnough = True
while True:
    if bigEnough:
        bigEnough = False
        options()

    WhatToDo = takeIn()

    match WhatToDo:
        case 'e':
            saveAndClose()
            break
        case '1':
            addReminder(WhatToDo)
        case '2':
            print("two sama")
        case _:
            print("tring to comprehend what u meant by that...")
            if addReminder(WhatToDo):
                print("bad bad input")
