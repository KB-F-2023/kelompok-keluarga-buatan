class Node:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.state < other.state
    
    def __hash__(self):
        return hash(str(self.state))


class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def find_blank_square(self, state):
        return state.index(0)

    def actions(self, state):
        blank_square = self.find_blank_square(state)
        actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        if blank_square % 3 == 0:
            actions.remove('LEFT')
        if blank_square < 3:
            actions.remove('UP')
        if blank_square % 3 == 2:
            actions.remove('RIGHT')
        if blank_square > 5:
            actions.remove('DOWN')
        return actions

    def result(self, state, action):
        blank_square = self.find_blank_square(state)
        new_state = state[:]
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank_square + delta[action]
        new_state[blank_square], new_state[neighbor] = new_state[neighbor], new_state[blank_square]
        return new_state

    def h1(self, state):
        return sum([1 if state[i] != self.goal[i] else 0 for i in range(9)])

    def solve(self):
        start_node = Node(self.start)
        pq = [start_node]
        visited = set()
        while pq:
            pq.sort(key=lambda x: x.depth + self.h1(x.state))
            node = pq.pop(0)
            if node.state == self.goal:
                path = []
                while node.parent:
                    path.append(node.move)
                    node = node.parent
                path.reverse()
                return path
            visited.add(node)
            for action in self.actions(node.state):
                child_state = self.result(node.state, action)
                child_node = Node(child_state, node, action)
                if child_node in visited:
                    continue
                pq.append(child_node)
        return None


if __name__ == '__main__':
    start = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    puzzle = Puzzle(start, goal)
    path = puzzle.solve()
    print(path)