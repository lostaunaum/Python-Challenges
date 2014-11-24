################## Student Grade Calculator ##################

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students =[lloyd, alice, tyler]

def average_grade(numbers):
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total 

def get_total_average_score(student):
    total = 0
    homework = average_grade(student["homework"])
    quizzes = average_grade(student["quizzes"])
    tests = average_grade(student["tests"])
    
    total += float(homework) * 0.10
    total += float(quizzes) * 0.30
    total += float(tests) * 0.60
    return total
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
    

#Average of one student
score = get_total_average_score(lloyd)
print score
print get_letter_grade(score)

#Class Average
class_average = get_class_average(students)
print class_average
print get_letter_grade(class_average)



################## Battle-Ship Against the AI ##################

from random import randint

#setting up the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
#these will be the coordinates of the computer hidden ship
ship_row = random_row(board)
ship_col = random_col(board)

print "Let's play Battleship! By Marco A. Lostaunau"

#game logic
for turn in range(5):
    #if user reaches 5 turns without successfully destroying ship user loses
    if turn == 4:
        print "Game Over"
        break
    
    print "Turn", turn + 1 #printing the current turn
    print_board(board)
    #prompting the user to ask for input
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    #if user guess is correct reacting
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        #making sure the guess is within the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
            turn -= 1
            
        #making sure the user does not guess same twice
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            turn -= 1
            
        #if not correct inform user print board again and set new x for the value
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"


################## Battle-Ship Player vs Player ##################

from random import randint

#setting up the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
#these will be the coordinates of the submarines from each player
player1_submarine_row = random_row(board)
player1_submarine_col = random_col(board)

player2_submarine_row = random_row(board)
player2_submarine_col = random_col(board)

if player1_submarine_row == player2_submarine_row:
    player2_submarine_row = random_row(board)
elif player1_submarine_col == player2_submarine_col:
    player2_submarine_col = random_col(board)

print "Let's play Battleship! By Marco A. Lostaunau"

#game logic
for turn in range(4):
    #we are giving the players a total of 4 turns
    if turn % 2 == 0: #player one will be even
        print "Player 1's turn", turn + 1 #printing the current turn
        print_board(board)
        #prompting the user to ask for input
        player1_guess_row = int(raw_input("Player 1 Guess Row:"))
        player1_guess_col = int(raw_input("Player 1 Guess Col:"))

        #if user guess is correct reacting
        if player1_guess_row == player2_submarine_row and player1_guess_col == player2_submarine_col:
            print "Congratulations! You sunk Player's 2 battleship!"
            break
        else:
            #making sure the guess is within the board
            if (player1_guess_row < 0 or player1_guess_row > 4) or (player1_guess_col < 0 or player1_guess_col > 4):
                print "Oops, that's not even in the ocean."
                turn -= 1
                
            #making sure the user does not guess same twice
            elif(board[player1_guess_row][player1_guess_row] == "X"):
                print "You guessed that one already."
                turn -= 1
                
            #if not correct inform user print board again and set new x for the value
            else:
                print "You missed Player's 2 battleship!"
                board[player1_guess_row][player1_guess_col] = "X"
    else: #players two logic going to try and combine it in one
        print "Player 2's turn", turn + 1 #printing the current turn
        print_board(board)
        #prompting the user to ask for input
        player2_guess_row = int(raw_input("Player 2 Guess Row:"))
        player2_guess_col = int(raw_input("Player 2 Guess Col:"))

        #if user guess is correct reacting
        if player2_guess_row == player1_submarine_row and player2_guess_col == player1_submarine_col:
            print "Congratulations! You sunk Player's 2 battleship!"
            break
        else:
            #making sure the guess is within the board
            if (player2_guess_row < 0 or player2_guess_row > 4) or (player2_guess_col < 0 or player2_guess_col > 4):
                print "Oops, that's not even in the ocean."
                turn -= 1
                
            #making sure the user does not guess same twice
            elif(board[player2_guess_row][player2_guess_row] == "-"):
                print "You guessed that one already."
                turn -= 1
                
            #if not correct inform user print board again and set new x for the value
            else:
                print "You missed Player's 1 battleship!"
                board[player2_guess_row ][player2_guess_col] = "-"

################## Battle-Ship Player vs Player ##################