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

    def _validate_input(self, input):
        """
        Validates the input for correctness.
        """
        if len(input) != self.positions:
            return False

        try:
            colors = [int(c) for c in input]
            return all(1 <= c <= self.colors for c in colors)
        except ValueError:
            return False

    def _get_hint(self, guess):
        """
        Generates a hint.
        """
        hint = []
        temp_solution = self.solution.copy()

        # Check for correct color and position
        for i in range(len(guess)):
            if guess[i] == temp_solution[i]:
                hint.append('*')
                temp_solution[i] = None  # Mark this position as matched

        # Check for correct color in wrong position
        for i in range(len(guess)):
            if guess[i] in temp_solution:
                hint.append('o')
                temp_solution[temp_solution.index(guess[i])] = None  # Mark this color as matched

        return ''.join(hint)
