class Mastermind:
    def __init__(self, colors, positions):
        self.colors = colors
        self.positions = positions
        self.solution = None
        self.guesses = []
