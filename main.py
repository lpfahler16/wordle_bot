from model.wordle_list_bot import WordleLetterBot2, WordleLetterBot, WordleRandomBot, WordleVowelBot
from model.wordle_wrapper_bot import WordleStarterBot, WordleRandomStarterBot
from view.wordle_view import WordleCommandLine
from view.wordle_gui import WordleHelpGUI, WordleHelpGUI2
from view.wordle_player import WordlePlayer
from controller.guess_help_controller import GuessHelpController


def main():
    best_helper()
    # first_helper()
    # auto_player()


def best_helper():
    bot = WordleLetterBot2()
    view = WordleHelpGUI2()
    controller = GuessHelpController(bot, view)
    controller.play()


def first_helper():
    bot = WordleLetterBot()
    view = WordleCommandLine()
    controller = GuessHelpController(bot, view)
    controller.play()


def auto_player():
    bot = WordleLetterBot2()
    view = WordlePlayer("array")
    controller = GuessHelpController(bot, view)
    controller.play()


if __name__ == "__main__":
    main()
