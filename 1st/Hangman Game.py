import random
random_words = ['mouse', 'key', 'house']
chosen_word = random.choice(random_words)
(number_of_attempts) = len(chosen_word)
print('number of letters and attempts is: ',number_of_attempts)
guess_the_word = input('Guess the Word:\n').lower()
for letter in guess_the_word:
    for words in chosen_word:
        print(words[0:len(chosen_word)])
    if guess_the_word == chosen_word:
        print('Right')
        print('The word you guessed:',guess_the_word)
        print('The answer is:', words)
    else:
        print("Wrong")
        print('The word you guessed:', letter)
        print('The answer is:', words)




