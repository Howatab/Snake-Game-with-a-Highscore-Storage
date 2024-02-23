from turtle import Turtle,Screen
import time
from Snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)  

snake = Snake()
screen.listen()
screen.onkey(key="Up",fun=snake.Snake_up) 
screen.onkey(key="Down",fun=snake.Snake_down)
screen.onkey(key="Left",fun=snake.Snake_left)
screen.onkey(key="Right",fun=snake.Snake_right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.Snake_forward()
    game_over = snake.Snake_collision_check()
    snake.Food_on_screen()
    
    
    
    
screen.exitonclick()