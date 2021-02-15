# Q3.py
# Jianan Lei
# 001058735
'''
game state
O | O | X
----------
X |   | O
----------
  |   | X
  
X turn
(["O", "O", "X", "X", None, "O", None, None, "X"], 1)
'''

def utility(state):
    #All 8 possible winer pattern
    winPattern = ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])
    
    X_index = [i for i, x in enumerate(state[0]) if x == "X"]
    O_index = [i for i, x in enumerate(state[0]) if x == "O"]
    for pattern in winPattern:
        if all(index in X_index for index in pattern):
            return 1
    
        if all(index in O_index for index in pattern):
            return -1
    
    if len(X_index) + len(O_index) == 9:
        return 0
    else:
        return None

def successor(state):
    blank = [i for i, x in enumerate(state[0]) if x == None]
    player = state[1]
    successorState = []
    for index in blank:
        temp = [ele for ele in state[0]]
        if player:
            temp[index] = "X"
            successorState.append((temp, 0))
        else:
            temp[index] = "O"
            successorState.append((temp, 1))
    return tuple(successorState)

def value(state):
    if utility(state) != None:
        return utility(state),state[0]
    if state[1]:
        return maxVal(state)
    else:
        return minVal(state)

def maxVal(state):
    v = float("-inf")
    bestMove = []
    for successorState in successor(state):
        temp = value(successorState)[0]
        #print(temp)
        if temp > v or temp == 1:
            bestMove.append(successorState[0])
        v = max(v, temp)
    return v, bestMove

def minVal(state):
    v = float("inf")
    bestMove = []
    for successorState in successor(state):
        temp = value(successorState)[0]
        #print(temp)
        if temp < v and v != float("inf") or temp == 0:
            bestMove.append(successorState[0])
        v = min(v, temp)
    return v, bestMove



# Test cases for utility
testCases1 = ((["O", "O", "X", "X", None, "O", None, None, "X"], 1), #None
              (["O", "O", "O", "X", "X", "O", None, None, "X"], 1), #-1
              (["O", "O", "X", "X", "X", "O", "X", None, "X"], 1), #1
              (["O", "O", "X", "X", "X", "O", "O", "X", "X"], 1)) #0
#for case in testCases1:
#    print "Case Result: "
#    print utility(case)

# Test cases for successor
testCases2 = ((["O", "O", "X", "X", None, "O", None, None, "X"], 1), #None
              (["O", "O", "O", "X", "X", "O", None, None, "X"], 0), #-1
              (["O", "O", "X", "X", "X", "O", "X", None, "X"], 1)) #0
# for case in testCases2:
    # print "Successor: "
    # print successor(case)

# Test cases for minimax
testCases3 = ((["O", "O", None, "X", None, None, None, None, "X"], 1), #1
              (["O", "O", "X", "X", "O", "O", "X", None, "X"], 0), #-1
              ([None]*9, 1)) #0
# for case in testCases3:
    # print "Result: "
    # print value(case)

#test = ([None, "O", None, None, None, None, None, None, 'X'],1)
#print value(test)
