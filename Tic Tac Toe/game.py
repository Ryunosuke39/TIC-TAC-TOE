class TicTacToe:
    def __init__(self):
        # the following called list comprehension, the concise way to create list
        # we iterate over place holder _ from 0 to 9(exculsive), the the value prehend to for will be placed in placeholder postion 
        # self.board = [" "]*9 is refaring the same string obj, modifying them will affact all element, so use comprehension list 
        # for creating list filled with independent string obj
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track of winner

    def print_board(self): 
        # again another list comprehension, 
        # we iterate a variable row from  [self.board[i*3:(i+1)*3] for i in range(3)]
        # value row is placeholder, and will be overwritten in each iteration
        # what confusing here is the range also has for loop, staring with i == 0
        # self.board[0:3], this indicates elements in self.board between 0(inclusive) and 3(exlusive), 
        # meaning values at index 0, 1, 2 which is " "
        # now row is sub list holding same value as self.board from index 0, 1, 2

        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            #ex) list = ("A", "B", "C")
            #    listCopy = "#".join(list)
            #    output: A#B#C
            # so it will fill the gap between elements in the row with " | "
            # element is (" ", " ", " ")
            # " "|" "|" "
            print("| " + " | ".join(row) + " |")



test = TicTacToe()
test.print_board()