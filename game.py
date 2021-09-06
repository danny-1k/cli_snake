import os
import keyboard
import random
import time

from snake import Snake

class Game:
    def __init__(self,width=40,height=20):
        self.width = width
        self.height = height
        self.board = [['-' for col in range(width)] for row in range(height)]
        self.is_on = True
        self.score = 0

    def clear_screen(self):
        
        self.board = [['-' for col in range(self.width)] for row in range(self.height)]
        os.system('cls')

    def spawn_snake(self):
        '''
        spawns a snake with random co-ordinated
        '''
        x = random.randint(0,self.width-1)
        y = random.randint(0,self.height-1)
        self.snake = Snake(x=x,y=y,game=self)
        self.draw_snake()

    def spawn_food(self):
        '''
        spawns food with random co-ordinates
        if the co-ordinates are in the snakes co-ordinates, it'll respawn
        until it isn't
        '''
        def gen_food():
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            return [x,y]

        pos = gen_food()

        while pos in self.snake.body:
            pos = gen_food()
        self.food = pos
        self.draw_food()

    def draw_snake(self):
        '''
        Draws the snake on the screen
        '''
        for idx,pos in enumerate(self.snake.body):
            #The game should be over when the snake is in contact with itself
            # A way of checking would be to check if the current position
            #is in the snakes co-ordinates
            if str(self.snake.body).count(str(pos)) > 1:
                 self.is_on = False
            else:
                #Basically fancy stuff for making the snake
                #face the direction it's going
                if idx == 0 and self.current_action == 'w':
                    self.board[pos[1]][pos[0]] = '^'

                elif idx == 0 and self.current_action == 'a':

                    self.board[pos[1]][pos[0]] = '<'

                elif idx == 0 and self.current_action == 'd':

                    self.board[pos[1]][pos[0]] = '>'

                elif idx == 0 and self.current_action == 's':
                    self.board[pos[1]][pos[0]] = 'V'

                else:
                    self.board[pos[1]][pos[0]] = '+'
                


    def draw_food(self):
        '''
        Display's the 'food' on the screen
        '''
        self.board[self.food[1]][self.food[0]] = '0'

    def update(self):
        '''
        Updates the current frame
        '''
        time.sleep(1/100)
        self.clear_screen()
        self.display()

    def set_current_action(self,act):
        '''
        Sets the current action (w,a,s,d)
        '''
        self.current_action = act

    def display_score(self):
        print('\n+------------+')
        print(f'| Score : {self.score}  |')
        print('+------------+')

    def display(self):
        self.draw_snake()
        self.draw_food()
        for row in self.board:
            print(''.join(row),end='\n')

    def take_action(self):
        actions = {'w':lambda x:self.set_current_action('w'),
                    's':lambda x:self.set_current_action('s'),
                    'a':lambda x:self.set_current_action('a'),
                    'd':lambda x:self.set_current_action('d'),
                    'up':lambda x:self.set_current_action('w'),
                    'down':lambda x:self.set_current_action('s'),
                    'left':lambda x:self.set_current_action('a'),
                    'right':lambda x:self.set_current_action('d'),
                    }

        for key in actions:
            #binding the key the the corresponding action
            keyboard.on_press_key(key,actions[key],suppress=True)

    def move(self):
        if self.current_action == 'w':
            self.snake.move_up()
        if self.current_action == 's':
            self.snake.move_down()
        if self.current_action == 'a':
            self.snake.move_left()
        if self.current_action == 'd':
            self.snake.move_right()

        time.sleep(1/10)

    def start(self):
        self.current_action = 'w'
        self.spawn_snake()
        self.spawn_food()
        while self.is_on:
            self.update()
            self.display_score()
            self.take_action()
            self.move()
        print('GAME OVER')