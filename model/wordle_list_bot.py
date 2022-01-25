from english_words import english_words_lower_alpha_set as ews
from model.buffed_list import BuffedList as BL


class WordleListBot(object):
    """A wordle bot that chooses words based on a stack of words"""

    def __init__(self, words):

        # info needed
        self.sorted_words = words
        self.gray = set()
        self.yellow = set()
        self.green = set()

    def index_of_word(self, word):
        i = 0
        while i < len(self.sorted_words):
            if self.sorted_words[i][0] == word:
                return i
            i += 1
        raise ValueError("Word " + word + " is not in the list")

    def return_guess(self) -> str:
        while len(self.sorted_words) > 0:
            word = self.sorted_words.pop(0)
            valid = self.__valid_gray__(word) and self.__valid_green__(
                word) and self.__valid_yellow__(word)
            if valid:
                return word

        raise ValueError("Cannot guess word")

    def __valid_gray__(self, word):
        for l in word:
            if l in self.gray:
                return False
        return True

    def __valid_yellow__(self, word):
        for tup in self.yellow:
            letter = tup[0]
            ypos = tup[1]

            pos = BL(word).find_all(letter)
            if len(pos) == 0 or ypos in pos:
                return False
        return True

    def __valid_green__(self, word):
        for tup in self.green:
            letter = tup[0]
            ypos = tup[1]

            pos = BL(word).find_all(letter)
            if not ypos in pos:
                return False
        return True

    def recieve_feedback(self, guess: str, feedback: str):
        if len(feedback) != 5:
            return
        for i in range(5):
            if feedback[i] == '0':
                green_letters = map(lambda x: x[0], self.green)
                if not guess[i] in green_letters:
                    self.gray.add(guess[i])
            if feedback[i] == '1':
                self.yellow.add((guess[i], i))
            if feedback[i] == '2':
                self.green.add((guess[i], i))
                if guess[i] in self.gray:
                    self.gray.remove(guess[i])

    def game_over(self) -> bool:
        return len(self.green) == 5


class WordleLetterBot(WordleListBot):

    def __init__(self):

        words = []

        for word in ews:
            if len(word) == 5:
                words.append(word)

        how_often = {}

        for word in words:
            for l in word:
                count = how_often.get(l)

                if count == None:
                    how_often[l] = 1
                else:
                    how_often[l] = count + 1

        sorted_words = []

        for word in words:
            score = 0

            for l in word:
                count = how_often.get(l)
                score += how_often[l]

            if len(sorted_words) != 0:
                curr = sorted_words[0][1]  # The frequency of word
                i = 0

                while i < len(sorted_words) and curr > score:
                    i += 1
                    if i < len(sorted_words):
                        curr = sorted_words[i][1]

                sorted_words.insert(i, (word, score))
            else:
                sorted_words.append((word, score))

        # info needed
        final_words = [word[0] for word in sorted_words]
        super().__init__(final_words)


class WordleLetterBot2(WordleListBot):

    def __init__(self):

        words = []

        for word in ews:
            if len(word) == 5:
                words.append(word)

        how_often = {}

        for word in words:
            for l in word:
                count = how_often.get(l)

                if count == None:
                    how_often[l] = 1
                else:
                    how_often[l] = count + 1

        sorted_words = []

        for word in words:

            # Has the letter already been counted?
            seen = set()
            score = 0

            for l in word:
                count = how_often.get(l)

                if not l in seen:
                    score += how_often[l]
                    seen.add(l)

            if len(sorted_words) != 0:
                curr = sorted_words[0][1]  # The frequency of word
                i = 0

                while i < len(sorted_words) and curr > score:
                    i += 1
                    if i < len(sorted_words):
                        curr = sorted_words[i][1]

                sorted_words.insert(i, (word, score))
            else:
                sorted_words.append((word, score))

        # info needed
        final_words = [word[0] for word in sorted_words]
        super().__init__(final_words)


class WordleRandomBot(WordleListBot):

    def __init__(self):

        words = []

        for word in ews:
            if len(word) == 5:
                words.append(word)

        super().__init__(words)


class WordleVowelBot(WordleListBot):

    def __init__(self):

        words = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']

        for word in ews:
            if len(word) == 5:
                words.append(word)

        how_often = {}

        for word in words:
            for l in word:
                count = how_often.get(l)

                if count == None:
                    how_often[l] = 1
                else:
                    how_often[l] = count + 1

        for l in vowels:
            how_often[l] = how_often[l] * 2

        sorted_words = []

        for word in words:

            # Has the letter already been counted?
            seen = set()
            score = 0

            for l in word:
                count = how_often.get(l)

                if not l in seen:
                    score += how_often[l]
                    seen.add(l)

            if len(sorted_words) != 0:
                curr = sorted_words[0][1]  # The frequency of word
                i = 0

                while i < len(sorted_words) and curr > score:
                    i += 1
                    if i < len(sorted_words):
                        curr = sorted_words[i][1]

                sorted_words.insert(i, (word, score))
            else:
                sorted_words.append((word, score))

        # info needed
        final_words = [word[0] for word in sorted_words]
        super().__init__(final_words)
