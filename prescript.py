import time
import random
import string

def text_scrambler(text):
    character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+=_[]{}|;:,.<>?/~`'
    COlOUR_CODE = "\033[38;2;134;186;218m"
    current_text = [' ' for _ in text]
    for i in range(len(current_text)):
        for j in range(i, len(current_text)):
            current_text[j] = random.choice(character)
            print(f"\r{COlOUR_CODE}{''.join(current_text)}\033[0m", end='')
            time.sleep(1 / 3125)
        
        current_text[i] = text[i]
        print(f"\r{COlOUR_CODE}{''.join(current_text)}\033[0m", end='')
        time.sleep(1 / 3125)
    print()

Text_group = [
    'To ..., place your hands on the ground and pray.',
    'To ..., jump over and over again until you are tired.',
    'To ..., see green from a white wall.',
    'To ..., see the world in a different way.',
    'To ..., At work ,cut work the ear of the first person to fulminate aganist you.',
    'To ..., Pet quadrupedal animals five times a day.'
    'To ..., Do not eat anything for a day and a night.',
    'To ..., Return to your home this instant. You may leave once a dog barks in front of your house one time.',
    'Write a song for your eleventh neighbor down the road, then play tag with your eleventh neighbor down the road. You do not need to win. Time limit: 84 months.',
    'To ..., watch a movie that you have never seen before, and then write a review about it.',
    'To ..., write a poem about the beauty of nature, and then read it aloud in public.',
    'To ..., Within three days, knit scarf with butterfly pattern, and then give it to a stranger.',


]
while True:
    text_scrambler(random.choice(Text_group))
    