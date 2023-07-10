import random
words = input("Enter the words you want to study with a space in between them. Press enter once you're done typing. Type 'restart' and press enter to restart. ").split()
while len(words) < 1:
    words = input("Enter the words you want to study with a space in between them. Press enter once you're done typing. Type 'restart' and press enter to restart. ").split()
randomWord = random.choice(words)
word = ""
lives = 10
def restart():
    Words = input("Enter the words you want to study with a space in between them. Press enter once you're done typing. Type 'restart' and press enter to restart. ").split()
    while len(Words) < 1:
        Words = input("Enter the words you want to study with a space in between them. Press enter once you're done typing. Type 'restart' and press enter to restart. ").split()
    if Words == ["restart"]:
        restart()
    RandomWord = random.choice(Words)
    Wrd = ""
    livs = 10
    reset(Wrd, RandomWord, Words, livs)
def game(wrd, RoundWord, wrds, lives):
    guess = input("Guess a letter! ")
    if guess == "restart":
        restart()
    if guess in RoundWord and len(guess) >= 1:
        copy = list(wrd)
        for leter in guess:
            for index, letter in enumerate(RoundWord):
                if leter in letter:
                    copy[index] = leter
                    wrd = "".join(copy)
        print(wrd)
        if RoundWord == wrd:
            print("Correct!")
            Word = ""
            roundword = random.choice(wrds)
            Lives = 10
            reset(Word, roundword, wrds, Lives)
        else:
            game(wrd, RoundWord, wrds, lives)
    elif len(guess) < 1:
        game(wrd, RoundWord, wrds, lives)
    elif guess not in RoundWord:
        lives -= 1
        if lives > 0:
            print("Incorrect. Lives: " + str(lives) + ". Try again.")
            print(wrd)
            game(wrd, RoundWord, wrds, lives)
        else:
            print("Game over. The word was " + str(RoundWord) + ".")
def reset(Word, roundword, wrds, lives):
    while len(Word) < len(roundword):
        Word += "_"
    if len(Word) == len(roundword):
        print(Word)
        game(Word, roundword, wrds, lives)
if words == ["restart"]:
    restart()
reset(word, randomWord, words, lives)