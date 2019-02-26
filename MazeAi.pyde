from Tile import *
from Player import *
import time


grid = []

def setup():
    size(402,500)
    global grid,player,episodes,delay
    #--CREATE GRID---------------
    x,y=0,0
    w = 100
    episodes = 0
    for i in range(4):
        x = 0
        for j in range(4):
            grid.append(Tile(x,y,'E',w))
            x += w
        y += w
    #---INIT GRID--------------------
    delay=0.1
    player = Player(grid[0])
    player.currtile.id='P'
    reset()
    
def reset():
    global grid ,holes, target, player
    for i in grid:
        i.id='E'
    holes = [2,5,14]
    for i in holes:
        grid[i].id='H'
    player.currtile = grid[0]
    player.currtile.id='P'
    target = 3
    grid[target].id='T'
    
def step(ac):
    s = grid.index(player.currtile)
    newPos,reward,s_=None,None,None
    done = False
    if ac=='d':
        if s not in [15,14,13,12]:
            newPos = grid.index(player.currtile) + 4
    elif ac=='u':
        if s not in [0,1,2,3]:
            newPos = grid.index(player.currtile) - 4
    elif ac=='r':
        if s not in [3,7,11,15]:
            newPos = grid.index(player.currtile) + 1
    elif ac=='l':
        if s not in [0,4,8,12]:
            newPos = grid.index(player.currtile) -1

    if newPos != None:
        if newPos == target:
            reward = 1
            s_ = 0
            done=True
            return s,s_,reward,ac,done
        if newPos in holes:
            reward = -1
            s_ = 0
            done=True
        else:
            player.swap_tile(grid[newPos])
            reward = -0.04
            s_=newPos
            done=False
    else:
        reward = -0.04
        s_ = grid.index(player.currtile)
        done = False
        
    return s,s_,reward,ac,done

def draw():
    global episodes
    background(31)
    for i in grid:
        i.show()
    
    action = player.getAction(grid.index(player.currtile))
    s,s_,r,ac,done = step(action)
    player.learn(s,s_,r,ac)
    
    fill(255)
    textSize(20)
    text("Episode: "+str(episodes),5,430)
    text("Current Reward: "+str(r),5,460)
    text("Current Frame Delay: "+str(delay),5,490)

    
    if done==True:
        episodes += 1
        grid[target].id='T'
        reset()
        if episodes%4 == 0 and episodes != 0:
            if player.epsilon > 0.01:
                player.epsilon -= 0.01
    
    time.sleep(delay)
    
    
