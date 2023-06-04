import random
import hangman_art as art
import hangman_wordl as wl


word = random.choice(wl.words)
result = []
lives = 6
for _ in word:
    result.append("_")

print(art.logo)
print()
print(result)

while "_" in result:
    if lives > 0:
        inp = input("Guess a letter: ").lower()
        
        if inp in result:
            print(f"You've already chosen {inp}. Please choose a new word.")
        
        elif inp not in result:
            if inp in word:
                n1 = len(word)
                for a in range(n1):
                    b = word[a]
                    if b == inp:
                        result[a] = inp
                        a+=1
                        print(f"You guessed {inp}. {inp} is at possition {a+1} in the word.")
            elif inp not in word:
                print(f"{inp} not in word.")
                print(art.stages[lives-1])
                lives -= 1
            print(result)
            
            if "_" not in result:
              print("You win!")
              break

    else: 
        print("You lose")
        print(f"Answer is {word}")
        break
    
                
