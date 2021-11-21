ItsJustForfun = input("Hello my friend.\nim here to play a game with you\npleas choos a number between 1-100\nok? if you are ready plz enter something :")#I TRY TO EXPLAIN WHAT I AM DOING AND GET FEED BACK

up = 100#IN THE FIRST OUR RANGE IS 0-100 SO UP=100 AND DOWN=0
down = 0
while ItsJustForfun:#WE WANT TO TRY AGAIN AND AGAIN TO FIND THE CURRECT NUMBER
    hint = input("ok , is it your number  {0} ? \nif not , your number bigger than {0} or smaller? \n(t for thats my number /b for biger / s fo smaller) :\n".format(int((up+down)/2)))#GUSS NUMBER AND USER CAN ENTER T FOR CURRECT GUESS AND B,b OR S,s FOR HELP
    if hint in ['t' , 'T']:#OK IF THE GUSS IS RIGHT WE SHOULD SAY GOOF BYE AND CLOSE THE WHILE LOOP
        print("Wow , I win..! \n bye bye")
        break
    elif hint in ['b' , 'B']:#IF THE CURRECT NUMBER IS BIGGER THAN MY GUESS , WE TRY TO PUT NEW VALUE IN DOWN
        down = int((down+up)/2)#TRY TO MAKE BETTER RANGE
    elif hint in ['s' , 'S']:#IF THE CURRECT NUMBER IS SMALLER THAN MY GUESS , WE TRY TO PUT NEW VALUE IN UP
        up = int((down+up)/2)+#TRY TO MAKE BETTER RANGE
    elif hint == 'foadferdows':#ITS FOR FUN!ISNT IT?
        print("o-|-O-|-o-|-O-|-o-|-O-|-o-|-O-|-o-|-O-|-o-|-O-|-o")
    else:
        print("i cant undrestand , try again")#JUST FOR SURE
        pass

