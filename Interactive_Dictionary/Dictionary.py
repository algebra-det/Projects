import json , difflib           # we can also use from difflib import get_close_matches

#difflib is a library that is used to get get_close_matches() , SequenceMatches, etc

data = json.load(open("data.json"))

# TO check a word we gotta use :- data["rain"] , that's the syntax

def translate(w):
    w = w.lower()                    # To make the string all-lower case as in json file every thing is in lower string
    if w in data:                    # To check if the word is in json file or not
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif len(difflib.get_close_matches(w, data.keys())) > 0:        # Check if there's a match for the word
        close = difflib.get_close_matches(w, data.keys())
        taking = input("Did you mean %s instead ? \n Enter Y if yes, else press any key "%(close[0]))

        if taking.lower()=="y":             # if user inputs that the match is correct
            return data[close[0]]
        else:                               # if not correct
            return "The word doesn't exist. Please double check it "

    else:                            # If there's no such word or match
        return "The word doesn't exist. Please double check it "

def outputs(out):
    if type(out) == list:
        for item in output:
            print(item)
    else:
        print(output)

word = input("Enter word : ")

output = translate(word)
outputs(output)
