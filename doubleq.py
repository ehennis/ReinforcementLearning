def DoubleQQuestion1(iVal):
    if iVal == 0.5:
        print('Correct')
        print('  The max value in Q^A is at index 1')
        print('  The expected value at index 1 of Q^B is 0.5')
    else:
        print('Incorrect.')
        print('  First, you need to find the index of MAX(Q^A)')
        print('  Then, you find the expected value at that index in Q^B')
