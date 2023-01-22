import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

word_list = ["aardvark", "baboon", "camel"]
word = random.choice(word_list)
word_g = []
for _ in range(len(word)):
    word_g.append('_')
nr_lines = len(word)
nr_guess = 1
end_game = False
while not end_game and nr_guess <= 6:
    guess = input("Guess a letter: ").lower()
    found = False
    for i in range(len(word)):
        if word[i] == guess:
            word_g[i] = guess
            nr_lines = nr_lines - 1
            found = True
    if found == False:
        nr_guess = nr_guess + 1
    print(word_g)
    print(stages[-nr_guess])
    if nr_lines == 0:
        end_game = True
if end_game == True:
    print("You win!")
else:
    print("You lose!")
