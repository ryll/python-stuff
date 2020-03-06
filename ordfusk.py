
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
        lst[i][1] += round(sum(((letterCount[n][word[n]]-len(lst)/2)/len(lst))**2 for n in range(letters))**0.5,4)
    return sorted(lst, key=itemgetter(1), reverse=False)

def wordsort2(words):
    lst = [[word,0] for word in words]
    letterCount = [{x : 0 for x in alphabet} for _ in range(letters)]

    # Count occurences of letters at every position
    for word,value in lst:
        for i,valDict in enumerate(letterCount):
            valDict[word[i]] += 1

    for i,(word,value) in enumerate(lst):
        lst[i][1] += round(sum(letterCount[n][word[n]]/len(lst) for n in range(letters))/letters,4)
    return sorted(lst, key=itemgetter(1),reverse=True)

# letters = int(input("How many letters? "))
letters = 6
words = [word for word in saol if len(word) == letters]

# ostron giraff spraka skrapa skvalp ankare betala cigarr damask falang garage halare javars kabare lavart rabatt
# answer = choice(words)
answer = "legend"
guessed = [set() for _ in range(letters)]
correct = ['_']*letters
print()
print(len(words))
print(answer)

while True:
    print(" ".join(correct))
    print([wordsort(words)[n] for n in range(min(5,len(words)))])
    print([wordsort2(words)[n] for n in range(min(5,len(words)))])

    # Get guess
    while True:
        guess = input("Make a guess: ")
        if guess in words:
            words.remove(guess)
            break
        else:
            print("Not a valid word, try again")
            break

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
