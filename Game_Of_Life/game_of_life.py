
import numpy as np
import random

from os import system
import time

def draw(life):
    # this function draw the life is going on right now
    # if any cell is alive print 0
    # else print ' '
    for i in range(50):
        for j in range(50):
            if life[i][j] == 0:
                print(' ',end='')
            else:
                print('0',end='')
        print()
        
def next(life):
    # this function make next life(world)
    # with 3 law:
    #     1. any live cell will die , if more than 3 cell is live around it
    #     2. any dead cell will alive , if exactly 3 cell is live around iter
    #     3. any live cell will die , if less than 2 cell is live around it
    newlife = np.zeros((50,50))
    for i in range(50):
        for j in range(50):
            sum = 0
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    if a == i and b == j:
                        continue
                    sum += life[a%50][b%50]
            if int(sum) == 3 and life[i][j] == 0:
                newlife[i][j] = 1
            elif int(sum) ==2 and life[i][j] == 1:
                newlife[i][j] = 1
            elif int(sum) ==3 and life[i][j] == 1:
                newlife[i][j] = 1
            else:
                newlife[i][j] = 0
                
                

    return newlife
            
                

def main():
    print('Game of life , writer : Foad ferdows')
    time.sleep(3)
    #in the first we must create a new world
    life = np.zeros( (50, 50) )
    for i in range(50):
        for j in range(50):
            per = random.randint(0,100) / 10
            if per < 2 :
                life[i][j] = 1
            else:
                life[i][j] = 0


    while True:
        #in thos loop , first we clear the screen
        #and next , draw life and make new world
        system('clear')
        draw(life)
        life = next(life)
        time.sleep(1)




if __name__ == '__main__':
    main()