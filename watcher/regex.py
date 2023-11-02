import re
"""
i = 1
end = 0
for ara in found.groups():
    if ara:
        match i:
            case 1:
                # from start of string till hrs ex: 40h
                dataDict.update(
                    {"hrs": partOfStringWithGoodData[0:found.span(1)[0]]})
                end = found.span(1)[1]

            case 2:
                dataDict.update(
                    {"mins": partOfStringWithGoodData[end:found.span(2)[0]]})
                end = found.span(2)[1]
            case 3:
                dataDict.update(
                    {"days": partOfStringWithGoodData[end:found.span(3)[0]]})
                end = found.span(3)[1]
            case 4:
                dataDict.update(
                    {"weeks": partOfStringWithGoodData[end:found.span(4)[0]]})
                end = found.span(4)[1]
            case 5:
                dataDict.update(
                    {"months": partOfStringWithGoodData[end:found.span(5)[0]]})
                end = found.span(5)[1]
            case 6:
                dataDict.update(
                    {"years": partOfStringWithGoodData[end:found.span(6)[0]]})
                # end = found.span(6)[1]
    i = i + 1
"""
# gigaPattern = re.compile(
#     r"(?i)^((\d+)((?:h|hr|hrs|hour|hours)|(?:m|min|mins|minute|minutes)|(?:d|day|days)|(?:w|week|weeks)|(?:month|months)|(?:y|yr|yrs|year|years)))+")
# betterPattern = re.compile(
#     r"(?i)^((\d+)(h|hr|hrs|hour|hours|m|min|mins|minute|minutes|d|day|days|w|week|weeks|month|months|y|yr|yrs|year|years))+")
# evenbetterPattern = re.compile(
#     r"(?i)(^\d+(h|hr|hrs|hour|hours|m|min|mins|minute|minutes|d|day|days|w|week|weeks|month|months|y|yr|yrs|year|years))+")

# group 1 is hours
# group 2 is minutes
# group 3 is days
# group 4 is weeks
# group 5 is months
# group 6 is years


gigaPattern = re.compile(
    r"(?i)^(?:(?:(?:\d+)(?:(hours|hour|hrs|hr|h)|(minutes|minute|mins|min|m)|(days|day|d)|(weeks|week|w)|(months|month)|(years|year|yrs|yr|y)))+)$")


searchin = "40d33m30h"
found = gigaPattern.match(searchin)
# 1st and 2nd element of group 0 tupple
# refinedString = searchin[found.span(0)[0]:found.span(0)[1]]
# data = [a for a in found.groups() if a]
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


breakpoint()
