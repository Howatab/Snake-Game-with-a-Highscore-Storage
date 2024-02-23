from turtle import Turtle,Screen
from Snake import Snake

class Menu:
    def __init__(self):
        self.screen = Screen()
        self.color = self.screen.textinput("Color Of Snake","Which Color Do You want your Snake To be : ")
        self.difficulty = self.screen.textinput("Difficulty Level","Select a Difficulty Level easy/normal/hard")
        self.snake = Snake()
        