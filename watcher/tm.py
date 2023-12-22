import json
import re
import os
# import asyncio


def startUp() -> list:
    try:
        with open("bigData.json") as araFile:
            return json.load(araFile)
    except FileNotFoundError:
        with open("bigData.json", mode="w") as nyaFile:
            json.dump({}, nyaFile, indent=4)


def saveAndClose(savingDataList: list) -> None:
    print("saved successfully !")
    with open("bigData.json", mode="w") as araFile:
        json.dump(savingDataList, araFile, indent=4)


def options() -> None:
    print("""available options are 
                                    adds a reminder for default text 
                                    1 - check all reminders
                                    e - exit""")


gigaPattern = re.compile(
    r"(?i)^(?:(?:(?:\d+)(?:(hours|hour|hrs|hr|h)|(minutes|minute|mins|min|m)|"
    r"(days|day|d)|(weeks|week|w)|(months|month)|(years|year|yrs|yr|y)))+)$")
standard = ["mins", "hrs", "days", "weeks", "months", "years"]


def addReminder(searchin: str, reason: str = None) -> bool:
    try:

        found = gigaPattern.match(searchin)
        dataDict = {"mins": None, "hrs": None, "days": None,
                    "weeks": None, "months": None, "years": None}
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

        final_reason = f'''{f'{dataDict["days"]} days ' if dataDict["days"] else ''}{f'{dataDict["hrs"]} hours ' if dataDict["hrs"] else ''}{'and ' if (dataDict["days"] or dataDict["hrs"]) and dataDict["mins"] else ''}{f'{dataDict["mins"]} minutes ' if dataDict["mins"] else ''}ago you asked to be reminded of {f'{reason}' if reason else 'something!'}'''

        hrs = f'''{f'--ei hrs {dataDict["hrs"]} ' if dataDict['hrs'] else '--ei hrs 0 '}'''
        mins = f'''{f'--ei mins {dataDict["mins"]} ' if dataDict['mins'] else '--ei mins 0 '}'''
        days = f'''{f'--ei days {dataDict["days"]} ' if dataDict['days'] else '--ei days 0 '}'''
        weeks = f'''{f'--ei weeks {dataDict["weeks"]} ' if dataDict['weeks'] else '--ei weeks 0 '}'''
        months = f'''{f'--ei months {dataDict["months"]} ' if dataDict['months'] else '--ei months 0 '}'''
        years = f'''{f'--ei years {dataDict["years"]} ' if dataDict['years'] else '--ei years 0 '}'''
        temp = hrs + mins + days + weeks + months + years
        temp = f'am broadcast --user 0 -a nya.wryyy {temp}--es reason "{final_reason}"'
        os.system(temp)
        print(temp)
        return False


if __name__ == "__main__":
    DataList = startUp()
    printOptions = True
    while True:
        if printOptions:
            printOptions = False
            options()

        WhatToDo = input(": ")

        match WhatToDo:
            case 'e':
                saveAndClose()
                break
            case '1':
                pass
            case _:
                try:
                    temp, reason = WhatToDo.split(maxsplit=1)
                except ValueError:
                    reason = None
                    temp = WhatToDo
                if addReminder(temp, reason):
                    print("bad bad input")
