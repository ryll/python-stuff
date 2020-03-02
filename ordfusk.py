
from operator import itemgetter
from random import choice
from string import ascii_lowercase

alphabet = ascii_lowercase + "åäö"
   
saol = []
with open("SAOL_14_clean.txt", encoding="UTF-8") as f:
    for line in f:
        saol.append(line.rstrip())


def wordsort(words):
    lst = [[word,0] for word in words]
    letterCount = [{x : 0 for x in alphabet} for _ in range(letters)]

    # Count occurences of letters at every position
    for word,value in lst:
        for i,valDict in enumerate(letterCount):
            valDict[word[i]] += 1

    for i,(word,value) in enumerate(lst):
        lst[i][1] += round(sum(((letterCount[n][word[n]]-len(lst)/2)/len(lst))**2 for n in range(letters))**0.5,2)
    return sorted(lst, key=itemgetter(1))

# letters = int(input("How many letters? "))
letters = 4
words = [word for word in saol if len(word) == letters]


answer = choice(words)
guessed = [set() for _ in range(letters)]
correct = ['_']*letters
print()
print(len(words))
print(answer)

while True:
    print(correct)
    print([wordsort(words)[n] for n in range(min(5,len(words)))])

    # Get guess
    while True:
        guess = input("Make a guess: ")
        if guess in words:
            words.remove(guess)
            break
        elif len(guess) != letters:
            print("Not a valid word, try again")
            continue
        else:
            print(f"Not a {letters} letter word, try again")
            continue

    if guess == answer:
        break

    for i in range(letters):
        guessed[i].add(guess[i])
        tempWords = words[:]
        if answer[i] == guess[i]:
            correct[i] = guess[i]
            for word in words:
                if word[i] != guess[i]:
                    tempWords.remove(word)
        else:
            for word in words:
                if word[i] == guess[i]:
                    tempWords.remove(word)
        words = tempWords[:]
    print(len(words))
    if '_' not in correct:
        break


"""
import locale
locale.setlocale(locale.LC_ALL, "sv_SE.UTF-8")
l.sort(key=locale.strxfrm)
"""