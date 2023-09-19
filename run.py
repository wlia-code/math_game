import random


class InputHandler:
    """
    Handles various types of user input
    """
    @staticmethod
    def get_int_input(prompt):
        """Prompt user for integer until a valid integer is entered"""
        while True:
            try:
                return int(input(f"\n{prompt}"))
            except ValueError:
                print("\nInvalid input Enter a number")

    @staticmethod
    def get_float_input(prompt):
        """Prompt user for float until a valid float is entered"""
        while True:
            try:
                return float(input(f"\n{prompt}"))
            except ValueError:
                print("\nInvalid input Enter a number")

    @staticmethod
    def get_yes_no_input(prompt):
        """Prompt user for a 'yes' or 'no' answer"""
        while True:
            answer = input(f"\n{prompt}").strip().lower()
            if answer in ['yes', 'no']:
                return answer
            else:
                print("\nInvalid input Enter 'yes' or 'no' ")


class MathGame:
    """
    Main class for Math Game, with methods for arithmetic operations
    and game logic
    """

    def __init__(self):
        self.score = 0
        self.wrong_attempts = 0
        self.input_handler = InputHandler()

    def play_game(self, difficulty, player_name):
        """Main game logic"""
        print('''\nInstructions: Solve the math problems
        You have 3 wrong attempts''')
        self.wrong_attempts = 0
        self.score = 0

        while self.wrong_attempts < 3:
            if difficulty == 10:  # Easy difficulty
                operation = random.choice(['+', '-', 'x'])
            else:
                operation = random.choice(['+', '-', 'x', '/'])

            operations = {
                '+': self.addition,
                '-': self.subtraction,
                'x': self.multiplication,
                '/': self.division
            }
            correct = operations[operation](difficulty)

            if correct:
                print("\nCorrect!")
                self.score += 1
            else:
                print("\nWrong!")
                self.wrong_attempts += 1
            print(f"\nYour current score is: {self.score}")

            if self.wrong_attempts >= 3:
                print("\nGame over! Max wrong attempts reached")
                break

        continue_game = self.input_handler.get_yes_no_input(
            "Continue playing? (yes/no) ")
        if continue_game == 'yes':
            self.play_game(difficulty, player_name)
        else:
            print(f'\nThanks 4 playing {player_name} final score {self.score}')

    def addition(self, difficulty):
        """Generate an addition question"""
        a = random.randint(1, difficulty)
        b = random.randint(1, difficulty)
        correct_answer = a + b
        user_answer = self.input_handler.get_int_input(f"What is {a} + {b}: ")
        return user_answer == correct_answer

    def subtraction(self, difficulty):
        """Generate a subtraction question"""
        a = random.randint(1, difficulty)
        b = random.randint(1, a)
        correct_answer = a - b
        user_answer = self.input_handler.get_int_input(f"What is {a} - {b}: ")
        return user_answer == correct_answer

    def multiplication(self, difficulty):
        """Generate a multiplication question"""
        a = random.randint(1, difficulty)
        b = random.randint(1, difficulty)
        correct_answer = a * b
        user_answer = self.input_handler.get_int_input(f"What is {a} x {b}: ")
        return user_answer == correct_answer

    def division(self, difficulty):
        """Generate a division question"""
        a = random.randint(1, difficulty)
        b = random.randint(1, difficulty)
        correct_answer = round(a / b, 2)
        user_answer = round(
            self.input_handler.get_float_input(
                f"What is {a} / {b} rounded to two decimal places: "
            ), 2
        )
        return user_answer == correct_answer


if __name__ == "__main__":
    print("\nWelcome to Math Game!")
    name = input("\nWhat's your name:\n ")
    print(f"\nHello, {name}!")

    print("\nDifficulty Levels: \n1. Easy \n2. Medium \n3. Hard")
    difficulty = InputHandler.get_int_input("Choose a difficulty level:\n")

    difficulty_mapping = {
        1: 10,
        2: 50,
        3: 100
    }
    game = MathGame()
    game.play_game(difficulty_mapping.get(difficulty, 10), name)
