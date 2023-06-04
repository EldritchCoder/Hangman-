import random
import hangman_art as art
import hangman_wordl as wl


word = random.choice(wl.words)
result = []
lives = 6
for _ in word:
    result.append("_")

print(art.logo)
print(result)

while "_" in result:
    if lives > 0:
        inp = input("Guess a letter: ").lower()
        if inp in word:
                n1 = len(word)
                for a in range(n1):
                    b = word[a]
                    if b == inp:
                        result[a] = inp
                        a+=1
                    else:
                        pass
                print(result)
                if "_" not in result:
                    print("You win!")
                    break

        elif inp not in word:
                print("wrong")
                print(art.stages[lives-1])
                lives -= 1

    else: 
        print("You lose")
        print(f"Answer is {word}")
        break
    
                