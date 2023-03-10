import random

# Generate a random initial state
def generate_initial_state(n):
    state = list(range(n))
    random.shuffle(state)
    return state

# Calculate the number of conflicts for a given state
def calculate_conflicts(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or i - state[i] == j - state[j] or i + state[i] == j + state[j]:
                conflicts += 1
    return conflicts

# Generate all possible successor states
def generate_successor_states(state):
    n = len(state)
    successors = []
    for i in range(n):
        for j in range(i + 1, n):
            successor = list(state)
            successor[i], successor[j] = successor[j], successor[i]
            successors.append(successor)
    return successors

# Choose the best successor state
def choose_best_successor(successors):
    n = len(successors[0])
    min_conflicts = calculate_conflicts(successors[0])
    best_successor = successors[0]
    for successor in successors[1:]:
        conflicts = calculate_conflicts(successor)
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            best_successor = successor
    return best_successor

# Solve the 8 Queens problem using local search with hill climb
def solve_8_queens(n):
    current_state = generate_initial_state(8)
    current_conflicts = calculate_conflicts(current_state)
    while current_conflicts > 0:
        successors = generate_successor_states(current_state)
        best_successor = choose_best_successor(successors)
        best_successor_conflicts = calculate_conflicts(best_successor)
        if best_successor_conflicts == current_conflicts:
            break
        current_state = best_successor
        current_conflicts = best_successor_conflicts
    return current_state

# Print the solution
def print_solution(solution):
    n = len(solution)
    for i in range(n):
        for j in range(n):
            if solution[j] == i:
                print("1 ", end="")
            else:
                print("0 ", end="")
        print()
    print()

if __name__ == "__main__":
    n = int(input("Masukkan jumlah test case: "))
    for _ in range(n):
        starting_state = solve_8_queens(8)
        print_solution(starting_state)
        print("Nilai Heuristics:", calculate_conflicts(starting_state))
        print()
