def QLQuestion1(iVal):
    if iVal == 0.638:
        print('Correct')
        print('  The old value is 0.1')
        print('  The learning rate (alpha) is 0.1')
        print('  The reward is 5')
        print('  The discount factor (gamma) is 0.8')
        print('  The max action from state S2 is A3 with a value of 0.6')
        print('  0.1 + 0.1 * (5 + 0.8 * 0.6 - 0.1)')
        print('  0.1 + 0.1 * (5 + 4.8 - 0.1)')
        print('  0.1 + 0.1 * (5.38)')
        print('  0.1 + 0.538')
        print('  0.638')
    else:
        print('Incorrect.')
        print('  The old value is 0.1')
        print('  The learning rate (alpha) is 0.1')
        print('  The reward is 5')
        print('  The discount factor (gamma) is 0.8')
        print('  The max action from state S2 is A3 with a value of 0.6')
        print('  0.1 + 0.1 * (5 + 0.8 * 0.6 - 0.1)')

def QLSolution1():
    print('Here is my solution')
    print('  Q[state][action] += alpha * (reward + gamma * Q[nstate].max() * (not done) - Q[state][action])')
