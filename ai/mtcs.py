import math
import time

from ai.AI import AI


class Node:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visited = 0
        self.score = 0

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_visited(self):
        return self.visited

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def set_visited(self, visited):
        self.visited = visited

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_all_possible_move())

    def select_child(self):
        exploration_factor = 1.4
        best_score = float("-inf")
        best_child = None
        for child in self.children:
            uct_score = child.get_score() / child.get_visited() + exploration_factor * \
                        math.sqrt(math.log(self.get_visited()) / child.get_visited())
            if uct_score > best_score:
                best_score = uct_score
                best_child = child
        return best_child

    def expand(self):
        untried_moves = [move for move in self.state.get_all_possible_move() if move not in
                         [child.get_state().last_move() for child in self.children]]
        random_move = untried_moves[0]
        self.state.make_move(random_move)
        child_node = Node(self.state, self)
        self.add_child(child_node)
        return child_node

    def simulate(self):
        while not self.state.game_over():
            self.state.make_move(self.state.get_all_possible_move()[0])
        return self.state.game_over()

    def backpropagate(self, result):
        self.visited += 1
        self.score += result
        if self.parent:
            self.parent.backpropagate(result)

    def uct_search(self, iterations):
        root_node = Node(self.state)
        for i in range(iterations):
            node = root_node
            while not node.is_fully_expanded() and not node.get_state().game_over():
                node = node.expand()
            result = node.simulate()
            node.backpropagate(result)
        best_child = root_node.select_child()
        print("MCTS: ", best_child.get_state().last_move().to_string())
        return best_child.get_state().last_move()


class MCTS(AI):
    def __init__(self):
        super().__init__()
        self.state = None
        self.root = None

    def AI_find_move(self, statement, valid_moves, depth=0):
        print("MCTS")
        self.state = statement
        start = time.time()
        if self.root and self.root.get_state().last_move() in valid_moves:
            self.update(self.root.get_state().last_move())
        else:
            self.root = Node(self.state)
        return self.root.uct_search(1000)

    def update(self, move):
        for child in self.root.get_children():
            if child.get_state().last_move() == move:
                self.root = child
                self.root.parent = None
                return
        self.root = Node(self.state)
