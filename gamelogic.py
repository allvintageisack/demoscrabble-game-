#class for computer player which inherits from player
class computerplayer(player):
    def generate_move(self):
        #it generates a random valid word,location and direction
        word = "TEST"
        location = [random.randint(0, 14), random.randint(0, 14)]
        direction = random.choice(["right","down"])
        return word,location,direction

def turn(player,board,bag):
    global round_number , players ,skipped_turns

    #if the game continues
    if (skipped_turns < 6) or (player.rack.get_rack_length() == 0 and bag.get_remaining_tiles() == 0):
        print("\nRound " + str(round_number)+": " + player.get_name() +"'s turn \n")
        print(board.get_board())
        print("\n" + player.get_name() + "'s Letter Rack:" + player.get_rack_str())

        if isinstance(player, computerplayer):
            # creates move for computer player 
            word_to_play, location , direction = player.generate_move()
            print(f"computer plays {word_to_play} at {location} {direction}")
        else:
            # human player plays 
            word_to_play = input("word to play: ")
            location = []
            col = input("colum number: ")
            row = input("Row number: ")  
            if(col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                location = [-1, -1]
            else:
                location = [int(row), int(col)]
            direction = input("Direction of words (right or down): ")

        word = word(word_to_play,location,player,direction,board.board_array())

        checked = word.check_word()
        while checked!= True:
            print(checked)
            if isinstance(player,computerplayer):
                #creates a new move if the previous one was invalid
                word_to_play,location ,direction = player.generate_move()
                print(f"Computer plays {word_to_play} at {location} {direction}")
            else:
                # Get new input from human player
                word_to_play = input("Word to play: ")
                word.set_word(word_to_play)
                location = []
                col = input("Column number: ")
                row = input("Row number: ")
                if (col == "" or row == "") or (col not in [str(x) for x in range(15)] or row not in [str(x) for x in range(15)]):
                    location = [-1, -1]
                else:
                    word.set_location([int(row), int(col)])
                    location = [int(row), int(col)]
                direction = input("Direction of word (right or down): ")
                word.set_direction(direction)
            checked = word.check_word()
        if word.get_word() == "":
            #skip turn if no valid word was given
            print("Turn skipped.")
            skipped_turns +=1

        else:
            #place a word on the board
            board.place_word(word_to_play,location,direction,player)
            word.calculate_word_score()
            skipped_turns = 0

        print("\n" + player.get_name() + "'s score is: " + str(player.get_score()))

       #get the next player!

        if players.index(player) != (len(players) -1):
            next_player = players[players.index(player)+1]
        else:
            next_player =players[0]
            round_number += 1

        #recursively(repeat!) call the turn function for the next player 
        turn(next_player, board,bag)
    else:
        #the game ends if conditions are not met
        end_game()
          
def start_game():
    global round_number, players, skipped_turns
    board = Board()
    bag = Bag() 

    num_of_players =int(input("\nPlease enter the number of players (1-4): "))
    while num_of_players< 1 or num_of_players > 4:
        num_of_players = int(input("This number is invalid. Please enter the number of players (1-4): "))

    print("\nWelcome to Scrabble! Please enter the names of the players below.")
    players = []
    for i in range(num_of_players):
        players.append(player(bag))
        players[i].set_name(input("Please enter player " + str(i+1) + "'s name: "))

    #adds computer player 
    players.append(ComputerPlayer(bag))
    players[-1].set_name("Computer")

    round_number = 1
    skipped_turns = 0
    current_player = players[0]
    turn(current_player, board, bag)

def end_game():
    global players
    highest_score = 0
    winning_player = ""
    for player in players:
        if player.get_score > highest_score:
            highest_score = player.get_score()
            winning_player = player.get_name()
    print("The game is over! " + winning_player + ", you have won!")

    if input("\nWould you like to play again? (y/n)").upper() == "Y":
        start_game()

start_game()



