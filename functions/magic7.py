from random import randint

def magic7():
    possible_replies = [
        "Uhhhh...", "...", "Ye",
        "¯\_(ツ)_/¯", "🤷", "🏀",
        "I dunno", "Errrr", "Indecisive",
        "I can't think right now, can you give me a minute?",
        "Magic 8 ball can you help me with this one?",
        "*screeching noises*", "Hey do you wanna go play basketball instead?",
        "https://tenor.com/bgNGq.gif", # Soup gif
        "https://tenor.com/bCL4U.gif", # Cat chair spinning gif
        "Джордж Констанс", # George Costanza in Ukrainian
        "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi1.kym-cdn.com%2Fphotos%2Fimages%2Foriginal%2F000%2F131%2F686%2Fimmahitu.jpg" # George Costanza picture
    ]

    return possible_replies[randint(0, len(possible_replies))]