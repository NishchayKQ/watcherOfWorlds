import json
import re
# import asyncio


def takeIn() -> str:
    ara = input(": ").replace("\n", "")
    return ara


def startUp() -> list:
    with open("bigData.json") as araFile:
        return json.load(araFile)


def saveAndClose(savingDataList: list) -> None:
    print("saved successfully !")
    with open("bigData.json", mode="w") as araFile:
        json.dump(araFile)


def options() -> None:
    print("""available options are 
                                    adds a reminder for default text 
                                    1 - check all reminders
                                    e - exit""")


hours = ("h", "hr",  "hrs", "hour", "hours")
mins = ("m", "min", "mins", "minute", "minutes")
secs = ("s", "sec", "seconds")
hours = re.compile("hr")


def addReminder(whatToDo) -> bool:  # opton 1
    if hours in whatToDo:
        print("kono dio da")

    if whatToDo == "bad data in input and cant process it":
        return True


DataList = startUp()
printOptions = True
while True:
    if printOptions:
        printOptions = False
        options()

    WhatToDo = takeIn()

    match WhatToDo:
        case 'e':
            saveAndClose()
            break
        case '1':
            pass
        case _:
            print("tring to comprehend what u meant by that...")
            if addReminder(WhatToDo):
                print("bad bad input")
