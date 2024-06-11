#class for computer player which inherits from player
class ComputerPlayer(Player):
    def generate_move(self):
        #it generates a random valid word,location and direction
        word = "TEST"
        location = [random.randint(0, 14), random.randint(0, 14)]
        direction = random.choice(["right","down"])
        return word,location,direction

def turn(player,board,bag):
    # Begin a turn, display the current board, get the information to play a turn, and create a loop for the next turn
    global round_number , skipped_turns

    #game continueation conditions
    if (skipped_turns < 6) or (len(player.rack) == 0 and len(bag.bag) == 0):
        print("\nRound " + str(round_number)+": " + player.name() +"'s turn \n")
        board.display_board()
        print(player.display_rack())

        if isinstance(player, ComputerPlayer):
            # computer player generates a move
            word_to_play, location , direction = player.generate_move()
            print(f"computer plays {word_to_play} at {location} {direction}")
        else:
            # human player plays 
            word_to_play = input("word to play: ") .upper()
            location = []
            col = input("colum number: ")
            row = input("Row number: ")  
            if(col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                location = [int(row), int(col)]
            direction = input("Direction of words (right or down): ").lower()

    #checks if thr word is valid
        word = Word(word_to_play, location, player, direction, board.board)
        checked = word.check_word()

        while not checked:
            print(checked)
            if isinstance(player,ComputerPlayer):
                #creates a new move if the previous one was invalid
                word_to_play,location ,direction = player.generate_move()
                print(f"Computer plays {word_to_play} at {location} {direction}")
            else:
                # Get new input from human player
                word_to_play = input("Word to play: ").upper()
                word.set_word(word_to_play)
                location = []
                col = input("Column number: ")
                row = input("Row number: ")
                if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                    location = [-1, -1]
                else:
                    word.set_location([int(row), int(col)])
                    location = [int(row), int(col)]
                direction = input("Direction of word (right or down): ").lower()
                word.set_direction(direction)
            checked = word.check_word()

        if word.get_word() == "":
            #skip turn if no valid word was given
            print("Turn skipped.")
            skipped_turns +=1

        else:
            #place a word on the board
            board.update_board(word_to_play, direction, location[1], location[0])
            word.calculate_word_score()
            player.remove_tiles(word_to_play)  # Remove tiles used in the word
            player.refill_rack(7 - len(player.rack))  # Refill the rack
            skipped_turns = 0

        print("\n" + player.name + "'s score is: " + str(player.get_score()))
        if isinstance(player, ComputerPlayer):
            print("Computer's score is: " + str(players[-1].get_score()))  # Display computer's score

        # Determine next player
        if players.index(player) != (len(players) - 1):
            next_player = players[players.index(player) + 1]
        else:
            next_player = players[0]
            round_number += 1

        # Recursive call for next player's turn
        turn(next_player, board, bag)
    else:
        end_game()
     
def start_game():
    # Start the game and call the turn function
    global round_number, players, skipped_turns
    board = Board()
    bag = TileBag(tiles)

    num_of_players = int(input("\nIf 1 + 1 = 2, what is 2 - 1 = "))
    while num_of_players != 1:
        num_of_players = int(input("Sorry, try again. You don't need Magic. What is 2 - 1 = "))
    print("Correct! Now we can proceed.")

    
    print("\nWelcome to Scrabble! Please enter your name.")
    players = []
    for i in range(num_of_players):
        player_name = input("Please enter player " + str(i + 1) + "'s name: ")
        players.append(Player(player_name))
    
    # Add computer player
    players.append(ComputerPlayer("Computer"))
    
    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score() > highest_score:
            highest_score = player.get_score()
            winning_player = player.name
    print("The game is over! " + winning_player + ", you have won!")
    
    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()

if _name_ == "_main_":
    start_game()





