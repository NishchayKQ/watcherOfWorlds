import re

gigaPattern = re.compile(
    r"(?i)^(\d+)((?:h|hr|hrs|hour|hours)|(m|min|mins|minute|minutes))")

# ("(d|day|days)(w|week|weeks)(month|months)(y|yr|yrs|year|years)")
searchin = "40h30m"
found = gigaPattern.search(searchin)

print(found.group(2))
