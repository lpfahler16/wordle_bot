# wordle_wrapper_bot.py
import random


class WordleWrapperBot(object):

    def __init__(self, bot):
        self.bot = bot

    def index_of_word(self, word):
        return self.bot.index_of_word(word)

    def return_guess(self):
        return self.bot.return_guess()

    def recieve_feedback(self, guess, feedback):
        self.bot.recieve_feedback(guess, feedback)

    def game_over(self):
        return self.bot.game_over()


class WordleStarterBot(WordleWrapperBot):

    def __init__(self, bot, starter):
        super().__init__(bot)
        bot.sorted_words.insert(0, starter)


class WordleRandomStarterBot(WordleWrapperBot):

    def __init__(self, bot):
        super().__init__(bot)
        i = random.randrange(len(bot.sorted_words))
        bot.sorted_words.insert(0, bot.sorted_words.pop(i))
