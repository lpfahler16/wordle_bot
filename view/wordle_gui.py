import PySimpleGUI as sg


class WordleHelpGUI(object):

    def __init__(self):
        # Create the window
        buttons = []
        for i in range(5):
            buttons.append(
                sg.Button("", key=i, button_color=('white', '#3a3a3c'), font='Arial 100', size=(2, 1)))

        layout = [buttons, [sg.Button("Submit", key="submit"), sg.Button(
            "Invalid", key="invalid"), sg.Button("Correct", key="correct")]]
        self.window = sg.Window("Wordle Helper", layout, finalize=True)
        self.feedback = [0, 0, 0, 0, 0]
        self.colors = ['#3a3a3c', '#b59f3b', '#538d4e']

    def update_guess(self, guess):
        self.feedback = [0, 0, 0, 0, 0]
        self.__update_button_colors__()
        for i in range(5):
            self.window.Element(i).update(guess[i])

    def get_feedback(self):
        while True:
            event, values = self.window.read()
            if event == 'submit':
                return "".join(map(lambda x: str(x), self.feedback))

            if event == 'invalid':
                return 'x'

            if event == 'correct':
                return '22222'

            self.feedback[event] = (self.feedback[event] + 1) % 3
            self.__update_button_colors__()

    def __update_button_colors__(self):
        for i in range(5):
            color = self.colors[self.feedback[i]]
            self.window[i].update(
                button_color=('white', color))

    def game_over(self):
        self.window.close()
