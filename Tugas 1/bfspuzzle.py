from queue import Queue

def bfs(initialState, goalState):
    bfsqueue = Queue()
    bfsqueue.put(initialState)
    visited = set()
    path = {tuple(initialState):None}
    
    while not bfsqueue.empty():
        currentState = bfsqueue.get()

        if currentState == goalState:
            SolvedPath = []
            while currentState is not None:
                SolvedPath.append(currentState)
                currentState = path.get(tuple(currentState))
            SolvedPath.reverse()
            return SolvedPath
        
        visited.add(tuple(currentState))

        for move in possibleMoves(currentState):
            newState = makeMoves(currentState, move)
            if tuple(newState) not in visited:
                bfsqueue.put(newState)
                path[tuple(newState)] = currentState
        
    return None

def possibleMoves(state):
    moves = []
    index = state.index(0)
    if index not in [0, 1, 2]: #up
        moves.append(-3)
    if index not in [2, 5, 8]: #right
        moves.append(1)
    if index not in [6, 7, 8]: #down
        moves.append(3)
    if index not in [0, 3, 6]: #left
        moves.append(-1)
    return moves

def makeMoves(state, move):
    new_state = state[:]
    index = state.index(0)
    new_index = index + move
    new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
    return new_state

initialState = [int(i) for i in input("Masukkan initial state:").split()]
goalState = [int(i) for i in input("Masukkan goal State:").split()]
solutionPath = bfs(initialState, goalState)
if solutionPath is not None:
    count = 0
    for state in solutionPath:
        if count == 0: print("Initial State")
        else: print("Iterasi ke-" + str(count))
        count = count + 1
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else: print("Tidak ditemukan solusi")