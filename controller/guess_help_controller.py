# guess_help_controller.py

class GuessHelpController(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play(self):
        while True:
            guess = self.model.return_guess()
            self.view.update_guess(guess)
            feedback = self.view.get_feedback()
            self.model.recieve_feedback(guess, feedback)
            if self.model.game_over():
                break
        self.view.game_over()
