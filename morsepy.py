# morse code translator v0.1 © Jameson Sisk 2022

# current functions: morsepy.morse, morsepy.morse_spaced

# "letters" is the information the translator draws from, essentially how it tells what letters and numbers to convert
letters = {
    "a": {
        "alphabet": "a",
        "morse": "._"
    },
    "b": {
        "alphabet": "b",
        "morse": "_..."
    },
    "c": {
        "alphabet": "c",
        "morse": "_._."
    },
    "d": {
        "alphabet": "d",
        "morse": "_.."
    },
    "e": {
        "alphabet": "e",
        "morse": "."
    },
    "f": {
        "alphabet": "f",
        "morse": ".._."
    },
    "g": {
        "alphabet": "g",
        "morse": "__."
    },
    "h": {
        "alphabet": "h",
        "morse": "...."
    },
    "i": {
        "alphabet": "i",
        "morse": ".."
    },
    "j": {
        "alphabet": "j",
        "morse": ".___"
    },
    "k": {
        "alphabet": "k",
        "morse": "_._"
    },
    "l": {
        "alphabet": "l",
        "morse": "._.."
    },
    "m": {
        "alphabet": "m",
        "morse": "__"
    },
    "n": {
        "alphabet": "n",
        "morse": "_."
    },
    "o": {
        "alphabet": "o",
        "morse": "___"
    },
    "p": {
        "alphabet": "p",
        "morse": ".__."
    },
    "q": {
        "alphabet": "q",
        "morse": "__._"
    },
    "r": {
        "alphabet": "r",
        "morse": "._."
    },
    "s": {
        "alphabet": "s",
        "morse": "..."
    },
    "t": {
        "alphabet": "t",
        "morse": "_"
    },
    "u": {
        "alphabet": "u",
        "morse": ".._"
    },
    "v": {
        "alphabet": "v",
        "morse": "..._"
    },
    "w": {
        "alphabet": "w",
        "morse": ".__"
    },
    "x": {
        "alphabet": "x",
        "morse": "_.._"
    },
    "y": {
        "alphabet": "y",
        "morse": "_.__"
    },
    "z": {
        "alphabet": "z",
        "morse": "__.."
    },
    "1": {
        "alphabet": "1",
        "morse": ".____"
    },
    "2": {
        "alphabet": "2",
        "morse": "..___"
    },
    "3": {
        "alphabet": "3",
        "morse": "...__"
    },
    "4": {
        "alphabet": "4",
        "morse": "...._"
    },
    "5": {
        "alphabet": "5",
        "morse": "....."
    },
    "6": {
        "alphabet": "6",
        "morse": "_...."
    },
    "7": {
        "alphabet": "7",
        "morse": "__..."
    },
    "8": {
        "alphabet": "8",
        "morse": "___.."
    },
    "9": {
        "alphabet": "9",
        "morse": "____."
    },
    "0": {
        "alphabet": "0",
        "morse": "_____"
    }
}

def morse(input): # this is for an output with no spaces between letters
    user_words = input.split()
    user_letters = []
    working_letters = []
    morse_list = []
    for word in user_words:
        part = " ".join(word)
        final_product = part.split()
        user_letters.append(final_product)
    for item in user_letters:
        for thing in item:
            working_letters.append(thing)
    for something in working_letters:
        for letter in letters:
            if something.lower() == letter:
                holder = letters[letter]["morse"]
                morse_list.append(holder)
    final_output = "".join(morse_list)
    print(final_output)

def morse_spaced(input): # this is for an output with spaces between letters
    user_words = input.split()
    user_letters = []
    working_letters = []
    morse_list = []
    for word in user_words:
        part = " ".join(word)
        final_product = part.split()
        user_letters.append(final_product)
    for item in user_letters:
        for thing in item:
            working_letters.append(thing)
    for something in working_letters:
        for letter in letters:
            if something.lower() == letter:
                holder = letters[letter]["morse"]
                morse_list.append(holder)
    final_output = " ".join(morse_list)
    print(final_output)
