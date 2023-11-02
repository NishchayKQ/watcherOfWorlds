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


gigaPattern = re.compile(
    r"(?i)^(?:(?:(?:\d+)(?:(hours|hour|hrs|hr|h)|(minutes|minute|mins|min|m)|(days|day|d)|(weeks|week|w)|(months|month)|(years|year|yrs|yr|y)))+)$")
standard = ["mins", "hrs", "days", "weeks", "months", "years"]


def addReminder(searchin: str) -> bool:  # opton 1
    try:
        found = gigaPattern.match(searchin)
        dataDict = {}
        i = 1
        for a in found.groups():
            if not a:
                i = i + 1
                continue
            match i:
                case 1:
                    dataDict.update(
                        {"hrs": re.search(fr"(\d+){a}", searchin).group(1)})
                case 2:
                    dataDict.update(
                        {"mins": re.search(fr"(\d+){a}", searchin).group(1)})
                case 3:
                    dataDict.update(
                        {"days": re.search(fr"(\d+){a}", searchin).group(1)})
                case 4:
                    dataDict.update(
                        {"weeks": re.search(fr"(\d+){a}", searchin).group(1)})
                case 5:
                    dataDict.update(
                        {"months": re.search(fr"(\d+){a}", searchin).group(1)})
                case 6:
                    dataDict.update(
                        {"years": re.search(fr"(\d+){a}", searchin).group(1)})
                case _:
                    print("critical error encountered 5535")
            i = i + 1
        # for ara in standard:
        #     dataDict.get(ara)

    except AttributeError:
        return True
    else:
        return False


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
