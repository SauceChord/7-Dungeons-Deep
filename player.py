
from direction import Direction
import turtle
import math
import random
import winsound


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(".\\art\\heroright.gif")
        self.penup()
        self.speed()
        self.fd(0)
        self.direction=Direction.right
        self.kill=0

    def setDirection(self, direction):
        self.direction = direction
        if direction == Direction.right:
            self.setheading(0)
        elif direction == Direction.up:
            self.setheading(90)
        elif direction == Direction.left:
            self.setheading(180)
        elif direction == Direction.down:
            self.setheading(270)

    def headright(self,proj,bob):

        if self.direction == Direction.right:
            pass
        self.setDirection(Direction.right)

        self.shape(".\\art\\heroright.gif")
        proj.shape(".\\art\\arrowright.gif")
        proj.fire(self,bob)


    def headdown(self,proj,bob):

        if self.direction == Direction.down:
            pass
        self.setDirection(Direction.down)
 
        self.shape(".\\art\\herodown.gif")
        proj.shape(".\\art\\arrowdown.gif")
        proj.fire(self,bob)

    def headleft(self,proj,bob):

        if self.direction == Direction.left:
            pass
        self.setDirection(Direction.left)

        self.shape(".\\art\\heroleft.gif")
        proj.shape(".\\art\\arrowleft.gif")
        proj.fire(self,bob)
            
    def headup(self,proj,bob):
          
        if self.direction == Direction.up:
            pass
        self.setDirection(Direction.up)
            
        self.shape(".\\art\\heroup.gif")
        proj.shape(".\\art\\arrowup.gif")
        proj.fire(self,bob)
 

    def go_up(self,block):

        if self.direction == Direction.up:
            pass
        self.setDirection(Direction.up)

        move_to_x = self.xcor()
        move_to_y = self.ycor()+24

        self.shape(".\\art\\heroup.gif")

        
        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
            

    def go_down(self,block):

        if self.direction == Direction.down:
            pass
        self.setDirection(Direction.down)
        
        move_to_x = self.xcor()
        move_to_y = self.ycor()-24
        self.shape(".\\art\\herodown.gif")
        
        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        
        
    def go_left(self,block):

        if self.direction == Direction.left:
            pass
        self.setDirection(Direction.left)
            
        move_to_x = self.xcor()-24
        move_to_y = self.ycor()
        self.shape(".\\art\\heroleft.gif")
        
        if (move_to_x, move_to_y) not in block :
            self.goto(move_to_x, move_to_y)
        
    def go_right(self,block):

        if self.direction == Direction.right:
            pass
        self.setDirection(Direction.right)
        
        move_to_x = self.xcor()+24
        move_to_y = self.ycor()


        if (move_to_x, move_to_y) not in block:
            self.goto(move_to_x, move_to_y)
        
        self.shape(".\\art\\heroright.gif")

          
    def drink(self,info):
        
        if info.potion>0 and info.hp is not info.fullhp : 
            info.potion-=1
            info.show_healthpotion()

            if info.hp < info.fullhp-300:
                info.hp+=300
                info.show_health()
            else:
                info.hp=info.fullhp
                info.show_health()
        else:
            pass
            
    def fireball(self,proj2,info,bob):
        if info.fire_scroll>0:
            info.fire_scroll-=1
            info.show_fire_scroll()
            proj2.fire(self,bob)
            
        else:
            pass
                 

    def is_collision(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 10:
            return True
        else:
            return False

    def is_collision2(self,other):
        a = self.xcor()- other.xcor()
        b = self.ycor()- other.ycor()
        distance = math.sqrt ((a ** 2)+(b ** 2) )

        if distance < 50:
            return True
        else:
            return False

    def destroy(self):
        self.goto(500,500)
        self.hideturtle()
