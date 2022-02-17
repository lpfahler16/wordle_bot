# wordle_player.py

class WordlePlayer(object):

    def __init__(self, word):
        self.word = word
        self.guess = ""
        self.num_guesses = 0

    def update_guess(self, guess: str):
        self.guess = guess
        self.num_guesses += 1
        print(self.guess)

    def get_feedback(self) -> str:
        feedback = []

        for i in range(5):
            l = self.guess[i]
            if l in self.word:
                if self.word[i] == l:
                    feedback.append('2')
                else:
                    feedback.append('1')
            else:
                feedback.append('0')
        print(''.join(feedback))
        return ''.join(feedback)

    def game_over(self):
        print("Yay! It took the bot " + str(self.num_guesses) + " guesses.")
