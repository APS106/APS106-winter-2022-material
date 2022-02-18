def print_guess(guess, color, incorrect_letters, i):
    """
    (str, str, incorrect_letters, int) -> None
    This function will generate a very fancy printing of the user's guess and its correctness.
    """

    white = "\x1b[0m"
    grey = "\x1b[47m"

    print(color + guess[i], end=" ")
    if i == (len(guess) - 1):
        print(white + '\t Incorrect Letters: ', end=" ")
        for j in sorted(incorrect_letters):
            print(grey + j, end=" ")
    print(white + '', end="")


def get_input_feedback(string, dictionary):
    """
    (str, enchant.Dict) -> None
    Check the string and provide feedback to the user.
    """

    if len(string) > 5:
        print('Your word is too long!')
    elif len(string) < 5:
        print('Your word is too short!')
    if dictionary.check(string) == False:
        print("This isn't a real word!")


def get_solution(dictionary):
    """
    (str) -> str
    Ask the player for a 5 letter word to guess and check if its valid.
    """
    solution = input('Give me a super secret 5-letter word: ')
    solution = solution.lower()

    while len(solution) != 5 or dictionary.check(solution) == False:
        get_input_feedback(solution, dictionary)
        solution = input('Give me a super secret 5-letter word: ')
        solution = solution.lower()

    return solution


def get_guess(attempts, dictionary):
    """
    (int) -> str
    Ask the player to guess a 5 letter word and check if its valid.
    """
    guess = input('Print Guess #' + str(7 - attempts) + ': ')
    guess = guess.lower()

    while len(guess) != 5 or dictionary.check(guess) == False:
        get_input_feedback(guess, dictionary)
        guess = input('Give me a new guess: ')
        guess = guess.lower()

    return guess


def check_guess(guess, solution, i):
    """
    (str, str, int) -> int, bool, str
    This function scores the user's guess and returns a color for some very fancy printing.

    Inputs:
    guess (str): The user's quess. e.g. "Apple"
    solution (str): The correct work. e.g. "Hello"
    i (int): The index of the current character being evaluated. For example, if i=2, the guess character is 'p'
             and the solution character is 'l'.

    Returns:
    int: This is the score, which is 1 if guess[i] == solution[i] and 0 if guess[i] != solution[i]
    bool: This is True is the guess character (guess[i]) is in the solution string.
          Example: True if guess[i] = 'e' and False if guess[i] = 'a'
    str: This is the color, which is green if guess[i] == solution[i], yellow if guess[i] == solution and otherwise grey.

    Example:
    1, True, green = check_guess("Apple", "Andie", 0)
    1, True, green = check_guess("Apple", "Andie", 4)
    0, False, yellow = check_guess("Apple", "Hello", 4)
    0, False, grey = check_guess("Apple", "Hello", 2)
    """
    green = "\x1b[42m"
    yellow = "\x1b[43m"
    grey = "\x1b[47m"

    if guess[i] == solution[i]:
        return 1, True, green
    elif guess[i] in solution:
        return 0, True, yellow
    else:
        return 0, False, grey


def play_wordle(dictionary):

    # Get the user solution
    solution = get_solution(dictionary)

    # Initialize some variables
    attempts = 6
    incorrect_letters = ""
    score = 0

    while (attempts > 0 and score != 5):

        score = 0

        guess = get_guess(attempts, dictionary)

        for i in range(0, len(guess)):

            points, correct_letter, color = check_guess(guess, solution, i)

            score += points

            if correct_letter is False and guess[i] not in incorrect_letters:
                incorrect_letters += guess[i]

            print_guess(guess, color, incorrect_letters, i)

        attempts = attempts - 1

    if (score == 5):
        print("Well done! You got the word " + solution)
    else:
        print("Better luck next time... the answer was: " + solution)
