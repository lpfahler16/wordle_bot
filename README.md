# wordle_bot

A python program made to help you win wordle. Controllers, views, and models are provided and can be extended to add new features.

## Working with the models

Every model has 3 methods:

```
def return_guess(self) -> str                           # Gives the next word the model is guessing
def recieve_feedback(self, guess: str, feedback: str)   # Gives the model feedback for a word, guess, formatted as a string with
                                                        # 0 for gray, 1 for yellow, and 2 for green (ex: 01020)
def game_over(self)                                     # Determines if the model has correctly guessed the word
```

## Working with the views
