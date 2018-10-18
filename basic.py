def MDPQuestion1(iVal):
    if iVal == "EESSS":
        print('Correct')
        print('  SENESSS took too many steps')
        print('  SEESS missed out on a +1 reward')
    elif iVal == "SENESSS":
        print('You took too many steps! Remember there is a negative time reward')
    else:
        print('Incorrect. Remember to collect as many rewards in as few passes as possible')
        
