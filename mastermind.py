class Mastermind:
    def __init__(self, colors, positions):
        self.colors = colors
        self.positions = positions
        self.solution = None
        self.guesses = []

    def setup_game(self):
        """
        Sets up the game with a random solution.
        """
        import random
        self.solution = [random.randint(1, self.colors) for _ in range(self.positions)]