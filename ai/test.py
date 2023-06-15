import random
import math

from state.state import State


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def expand(self):
        possible_moves = self.state.get_all_possible_move()
        for move in possible_moves:
            new_state = self.state.make_move(move)
            new_node = Node(new_state, parent=self)
            self.children.append(new_node)

    def select_child(self):
        exploration_factor = 1.4
        best_score = float("-inf")
        best_child = None
        for child in self.children:
            score = child.wins / child.visits + exploration_factor * math.sqrt(math.log(self.visits) / child.visits)
            if score > best_score:
                best_score = score
                best_child = child
        return best_child

    def simulate(self):
        current_state = self.state
        while not current_state.game_over():
            possible_moves = current_state.get_possible_moves()
            random_move = random.choice(possible_moves)
            current_state = current_state.make_move(random_move)
        return current_state.get_result()

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

class MCTS:
    def __init__(self, initial_state, exploration_budget):
        self.initial_state = initial_state
        self.exploration_budget = exploration_budget

    def search(self):
        root = Node(self.initial_state)
        for _ in range(self.exploration_budget):
            node = self.select_node(root)
            if not node.state.game_over():
                node.expand()
                if node.children:
                    child = random.choice(node.children)
                    result = child.simulate()
                    child.backpropagate(result)
        best_child = root.select_child()
        return best_child.state

    def select_node(self, node):
        while node.children:
            if not node.state.game_over():
                return node
            node = node.select_child()
        return node

# Các lớp State và Move tùy chỉnh cho trò chơi Tic-Tac-Toe
# Cần cài đặt các phương thức get_possible_moves, make_move, is_terminal, get_result cho lớp State

# Hàm chạy MCTS cho trò chơi Tic-Tac-Toe
def run_mcts():
    initial_state = State()
    mcts = MCTS(initial_state, exploration_budget=1000)
    final_state = mcts.search()
    # Xử lý kết quả cuối cùng

if __name__ == "__main__":
    run_mcts()
