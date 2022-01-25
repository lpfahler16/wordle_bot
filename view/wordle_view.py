# wordle_view.py

class WordleCommandLine(object):

    def __init__(self):
        pass

    def update_guess(self, guess: str):
        print(guess)

    def get_feedback(self) -> str:
        return input("Give feedback: ")

    def game_over(self):
        print("Yay!")
