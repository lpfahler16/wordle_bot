from model.wordle_list_bot import WordleLetterBot2, WordleLetterBot, WordleRandomBot, WordleVowelBot
from model.wordle_wrapper_bot import WordleStarterBot, WordleRandomStarterBot
from view.wordle_view import WordleCommandLine
from view.wordle_gui import WordleHelpGUI
from controller.guess_help_controller import GuessHelpController


def main():
    bot = WordleLetterBot2()
    view = WordleHelpGUI()
    controller = GuessHelpController(bot, view)
    controller.play()


if __name__ == "__main__":
    main()

### View methods ###
# update_guess: string -> void
# get_feedback: -> string
# game_over:
