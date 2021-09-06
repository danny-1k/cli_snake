class Snake:
    def __init__(self,x,y,game):
        self.game = game
        self.body = [[x,y]]
        self.last_pos = [x,y]

    def move_up(self):
        '''
        Method to move the snake up
        '''
        for idx in range(len(self.body)):
            if idx == 0:
                self.last_pos = [self.body[idx][0],self.body[idx][1]]
                self.body[idx][1]-=1
                print('Current Position : up')

                if self.body[idx][1] < 0:
                    #When the snake is going out of frame
                    #from the top, it should re-appear at the bottom
                    self.body[idx][1] = self.game.height -1

                if self.body[idx] == self.game.food:
                    # if the snake's on the food
                    #then another 'part' is added
                    #and the food is respawned
                    self.game.spawn_food()
                    self.game.score+=1
                    if self.body[-1][1] == (self.game.height-1):
                        #If the top of the screen is occupied by the snake,
                        #the body is continued from the bottom
                        self.body.append([self.body[-1][0],0])
                    else:
                        self.body.append([self.body[-1][0],self.body[-1][1]+1])
            
            else:
                last_pos = self.body[idx]
                self.body[idx] = self.last_pos
                self.last_pos = last_pos
            

    def move_down(self):
        '''
        Method to move the snake down
        '''
        for idx in range(len(self.body)):
            if idx == 0:
                self.last_pos = [self.body[idx][0],self.body[idx][1]]
                self.body[idx][1]+=1
                print('Current Position : down')
                if self.body[idx][1] > (self.game.height-1):
                    #When the snake is going out of frame
                    #from the bottom, it should re-appear at the top
                    self.body[idx][1] = 0

                if self.body[idx] == self.game.food:
                    self.game.spawn_food()
                    self.game.score+=1
                    if self.body[-1][1] == 0:
                        #If the bottom of the screen is occupied by the snake,
                        #the body is continued from the top
                        self.body.append([self.body[-1][0],(self.game.height-1)])
                    else:
                        self.body.append([self.body[-1][0],self.body[-1][1]-1])
                
            else:
                last_pos = self.body[idx]
                self.body[idx] = self.last_pos
                self.last_pos = last_pos

    def move_left(self):
        '''
        Method to move the snake left
        '''
        for idx in range(len(self.body)):
            if idx == 0:
                self.last_pos = [self.body[idx][0],self.body[idx][1]]
                self.body[idx][0]-=1
                print('Current Position : left')
                if self.body[idx][0] < 0:
                    #When the snake is going out of frame
                    #from the left, it should re-appear at the right                    
                    self.body[idx][0] = self.game.width - 1

                if self.body[idx] == self.game.food:
                    self.game.spawn_food()
                    self.game.score+=1
                    if self.body[-1][0] == (self.game.width - 1):
                        self.body.append([0,self.body[-1][1]-1])
                    else:
                        self.body.append([self.body[-1][0],self.body[-1][1]-1])
                
            else:
                last_pos = self.body[idx]
                self.body[idx] = self.last_pos
                self.last_pos = last_pos

    def move_right(self):
        '''
        Method to move the snake right
        '''
        for idx in range(len(self.body)):
            if idx == 0:

                self.last_pos = [self.body[idx][0],self.body[idx][1]]
                self.body[idx][0]+=1
                print('Current Position : right')

                if self.body[idx][0] > (self.game.width-1):
                    #When the snake is going out of frame
                    #from the right, it should re-appear at the left
                    self.body[idx][0] = 0

                if self.body[idx] == self.game.food:
                    self.game.spawn_food()
                    self.game.score+=1
                    if self.body[-1][0] == 0:
                        self.body.append([self.game.width - 1,self.body[-1][1]-1])
                    else:
                        self.body.append([self.body[-1][0],self.body[-1][1]+1])

            else:
                last_pos = self.body[idx]
                self.body[idx] = self.last_pos
                self.last_pos = last_pos