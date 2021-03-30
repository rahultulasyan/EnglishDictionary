import json
from difflib import get_close_matches


def translate(key):
    key = key.lower()
    if key in data:
        print(key.capitalize(), ":")
        return data[key]

    elif key.title() in data:
        return data[key.title()]

    elif key.upper() in data:
        return data[key.upper()]

    options = get_close_matches(key, data.keys(), cutoff=0.8)
    if len(options) > 0:
        ans = input("Did You Mean ** %s ** instead?, Enter 'Y' for YES: " %options[0]).upper()
        if ans == "Y":
            return data[options[0]]
        else:
            return ["Word Not Found !"]
    else:
        return ["Word Not Found !"]


data = json.load(open("data.json"))
word = input("Enter Word: ").lower()
definitions = translate(word)
for line in definitions:
    print(line)