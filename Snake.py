from turtle import Screen,Turtle
import time
import random

turtle_colors = ["white", "black", "gray", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "brown", "pink", "cyan", "magenta", "purple", "turquoise", "gold", "silver"]

class Snake:
    def __init__(self):
        self.Turtles = [Turtle() for _ in range(5)]
        self.align()
        self.food_on_screen = False
        self.food = self.generate_food()
        self.Player_score = 0
        self.score = Turtle()
        self.score.clear()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 270)
        self.score.color("red")
        self.highscore = 0
        self.read_highscore()
        self.score_counter()
        
        
    
    colors = ["red","blue","green","orange","cyan","brown","yellow"]
    
    def create_snakes(self):
        self.Turtles = [Turtle() for _ in range(5)]
        self.align()
    
    
    def align(self):
        for i, T in enumerate(self.Turtles):
            T.penup()
            T.goto(0 + (i * -20), 0)
            T.shape("square")
            T.speed(10)
            T.color('brown')
            self.Turtles[0].color('white')
            
    def Snake_out_of_bounds(self):
        if self.Turtles[0].xcor() < -290:
            self.Turtles[0].setx(290)
        elif self.Turtles[0].xcor() > 290:
            self.Turtles[0].setx(-290) 
        if self.Turtles[0].ycor() < -290:
            self.Turtles[0].sety(290)
        elif self.Turtles[0].ycor() > 290:
            self.Turtles[0].sety(-290) 
        

    def Snake_forward(self):
        for i in range(len(self.Turtles)-1,0,-1):
            if i%2 == 0 and not i == 0:
                self.Turtles[i].color("red")
            xcor = self.Turtles[i-1].xcor()
            ycor = self.Turtles[i-1].ycor()
            self.Turtles[i].goto(xcor,ycor)
        self.Turtles[0].forward(20)
        
        self.Snake_out_of_bounds()

    def read_highscore(self):
        with open("D:\SnakeGame\data.txt") as line:
            highscore = line.read()
            self.highscore = highscore
    def update_highscore(self):
        with open("D:\SnakeGame\data.txt", mode="w") as line:
            line.write(self.highscore)
    
    
    def Snake_up(self):
        if not self.Turtles[0].heading() == 270:
            
            self.Turtles[0].setheading(90)


    def Snake_down(self):
        if not self.Turtles[0].heading() == 90:
            
            self.Turtles[0].setheading(270)
        

    def Snake_left(self):
        if not self.Turtles[0].heading() == 0:
            
            self.Turtles[0].setheading(180)
        

    def Snake_right(self):
        if not self.Turtles[0].heading() == 180:
            
            self.Turtles[0].setheading(0)
    
    def Snake_length(self):
        xcor = self.Turtles[len(self.Turtles)-1].xcor()
        ycor = self.Turtles[len(self.Turtles)-1].ycor()
        heading = self.Turtles[len(self.Turtles)-1].heading()
        Extension = Turtle()
        Extension.penup()
        Extension.shape("square")
        Extension.color('white')
        Extension.speed(10)
        Extension.color('brown')
        Extension.setheading(heading)
        Extension.goto(xcor,ycor)
        self.Turtles.append(Extension)
        
        
    
    def generate_food(self):
        food = Turtle()
        food.penup()
        food.shape('circle')
        food.color('white')
        food.shapesize(0.5,0.5)
        food.goto(random.randint(1,260),random.randint(1,260))
        return food
    
    def Food_on_screen(self):
        if not self.food_on_screen:
            self.food_on_screen = True
        self.Food_eaten()
    
    def game_over(self):
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.color("red")
        turtle.write("Game Over", align="center", font=("Arial", 24, "normal"))
        turtle.goto(0, -30)
        turtle.write(f"Your Final Score = {self.Player_score}", align="center", font=("Arial", 16, "normal"))
    
    def reset(self):
        for T in self.Turtles:
            T.clear()
            T.goto(1000,1000)
        self.Turtles.clear()
        self.create_snakes()
        self.Player_score = 0
    
    def score_counter(self):
        self.score.clear()
        if self.Player_score > int(self.highscore):
            self.highscore = str(self.Player_score)
            self.update_highscore()
        text = f"Your Score = {self.Player_score} , HighScore = {self.highscore}"
        self.score.write(text, align="center", font=("Arial", 12, "normal"))
        
    
    def Snake_collision_check(self):
        head_position = self.Turtles[0].pos()
        for i in range(len(self.Turtles)-1):
            body_postion = self.Turtles[i].pos()
            if abs(head_position[0] - body_postion[0])<15 and abs(head_position[1]-body_postion[1]) <15 and not i == 0:
                return True
    
    
                
            
    
    def Food_eaten(self):
        if self.food_on_screen:
            snake_location = self.Turtles[0].pos()
            food_location = self.food.pos()
            if abs(snake_location[0]-food_location[0])<15 and abs(snake_location[1]-food_location[1])<15:
                    self.food_on_screen = False
                    self.food.setpos(random.randint(1,270),random.randint(1,270))
                    self.Snake_length()
                    self.Score_increment()
                    
                    
    def Score_increment(self):
        self.Player_score += 10
        