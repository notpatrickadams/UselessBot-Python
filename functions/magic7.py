from random import randint

def magic7_generate():
    possible_replies = [
        "Uhhhh...", "...", "Ye",
        "¯\_(ツ)_/¯", "🤷", "🏀",
        "I dunno", "Errrr", "Indecisive",
        "Brain hurt. Don't ask hard question",
        "Magic 8 ball can you help me with this one?",
        "*screeching noises*", "Hey do you wanna go play basketball instead?",
        "https://tenor.com/bgNGq.gif", # Soup gif
        "https://tenor.com/bCL4U.gif", # Cat chair spinning gif
        "Джордж Констанс", # George Costanza in Ukrainian
        "http://i1.kym-cdn.com/photos/images/original/000/131/686/immahitu.jpg" # George Costanza picture
    ]

    return possible_replies[randint(0, len(possible_replies))]