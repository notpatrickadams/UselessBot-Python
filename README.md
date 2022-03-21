# UselessBot

A useless Discord bot that generates pictures of bees!

## Installing & Running

```bash
pip3 install -r requirements.txt && python3 main.py
```

There will be a log at `bot.log`

## Commands

- !bee
  - Sends a really good drawing of a bee with random colors!
- !pokemon
  - Sends a random Pokemon in chat with types, flavor text, and the Dex number
  - 1/128 chance that the image of the Pokemon will be in shiny form
- The mention of the word "lamp"
  - Sends an image of a moth
    - Because moths love light sources

## To-Do

- Convert `!` commands to `/` commands with `discord-py-interactions`
- Make Pokemon with different forms display better
  - Currently it shows `name-form`
  - Solution: Add field for form if form is anything other than the default form 
