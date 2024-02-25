from turtle import Turtle,Screen
import time
import random
import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("The Snake Game")
screen.tracer(0)  

snake = Snake.Snake()
screen.listen()
screen.onkey(key="Up",fun=snake.Snake_up) 
screen.onkey(key="Down",fun=snake.Snake_down)
screen.onkey(key="Left",fun=snake.Snake_left)
screen.onkey(key="Right",fun=snake.Snake_right)

def Collision_effect():
    for x in range(len(snake.Turtles)):
            snake.Turtles[x].color(random.choice(Snake.turtle_colors))
            time.sleep(0.1)
            screen.update()
            snake.Turtles[x].forward(1000)
            time.sleep(0.1)
            screen.update()


game_over = False

while not game_over:
    screen.update()
    time.sleep(0.05)
    snake.Snake_forward()
    if snake.Snake_collision_check():
        Collision_effect()
        snake.reset()

    snake.Food_on_screen()
    snake.score_counter()
    
    
    
    
screen.exitonclick()