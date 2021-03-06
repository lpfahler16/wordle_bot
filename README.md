# wordle_bot

A python program made to help you win wordle. Controllers, views, and models are provided and can be extended to add new features.

## Working with the models

Every model has 3 methods:

```
def return_guess(self) -> str                           # Gives the next word the model is guessing
def recieve_feedback(self, guess: str, feedback: str)   # Gives the model feedback for a word, guess, formatted as a string with
                                                        # 0 for gray, 1 for yellow, and 2 for green (ex: 01020)
def game_over(self) -> bool                             # Determines if the model has correctly guessed the word
```

## Working with the views

Every view has 3 methods:

```
def update_guess(self, guess: str)                      # Tells the view what the most recent guess is
def get_feedback(self) -> str                           # Gets the feedback that the view has acquired
def game_over(self)                                     # Tells the view that the game is over
```

## Working with the controllers

Every controller has 1 method:

```
def play(self)                                          # Starts the play between the model and view
```
