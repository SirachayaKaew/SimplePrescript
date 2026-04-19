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

#Text_group = [
#    'Sentence',
#    'Sentence',
#    'Sentence',
#    'Sentence',
#    'Sentence',
#    'Sentence'
#    'Sentence',
#    'Sentence',
#    'Sentence',
#    'Sentence',
#    'Sentence',
#    'Sentence',


]
while True:
    text_scrambler(random.choice(Text_group))
    
