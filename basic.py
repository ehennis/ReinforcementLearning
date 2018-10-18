def MDPQuestion1(sVal):
    if sVal == "EESSS":
        print('Correct')
        print('  SENESSS took too many steps')
        print('  SEESS missed out on a +1 reward')
    elif sVal == "SENESSS":
        print('You took too many steps! Remember there is a negative time reward')
    else:
        print('Incorrect. Remember to collect as many rewards in as few moves as possible')
        
def MDPQuestion2(iVal):
    if iVal == 12:
        print('Correct')
        print('  These could be stored in a 1 x 12 array')
    else:
        print('Incorrect. Count the spaces. You have a 3x4 grid')

def MDPQuestion3(iVal):
    if iVal == 4:
        print('Correct')
        print('  N, E, S, and W for the cardinal directions')
    else:
        print('Incorrect. How many directions can you move?')

def MDPQuestion4(iVal):
    if iVal == 1:
        print('Correct')
        print('  If you select E you will move to the state to the right 100% of the time. Had this been a stochastic process you would need to account for that.')
    else:
        print('Incorrect. Where do you end up if you move right?')

def MDPQuestion5(iVal):
    if iVal == 0:
        print('Correct')
        print('  That action runs you into a wall and will not move to the state to the east')
    else:
        print('Incorrect. How can you move to the East by going North?')        

def MDPQuestion6(iVal):
    if iVal == 1:
        print('Correct')
        print('  You pick up the reward in that state when you enter it')
    else:
        print('Incorrect. What is the reward value of cell (2,0)?')

def MDPQuestion7(iVal):
    if iVal == -1:
        print('Correct')
        print('  You pick up the reward in that state when you enter it')
    else:
        print('Incorrect. What is the reward value of cell (0,2)?')          
