from tqdm import tqdm
from numba import jit
alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'

@jit
def caesar(text, offset):



    new_text = ''.join(
        alphabet[(alphabet.index(t) + 1) % len(alphabet)]
        if t in alphabet else t for t in text
    )
    
    if offset == 1:
        return new_text
    else:
        return caesar(new_text, offset - 1)

def caesar2(text, offset):
    return ''.join(
        alphabet[(alphabet.index(t) + offset) % len(alphabet)]
        if t in alphabet else t for t in text.lower()
    )

# print(caesar('hej jag heter ryll', 996))


with open("SAOL_14.txt", encoding="UTF-8") as f:
   for line in tqdm(f):
       caesar(line,500)



"""
import locale
locale.setlocale(locale.LC_ALL, "sv_SE.UTF-8")
l.sort(key=locale.strxfrm)
"""