# Goal of this Code: Lets Solve Puzzles!

# The Rules:
# Each puzzle piece has 4 sides, there are a total of n different inserters 
#  and n number of accepters. There are q puzzle pieces. Lets solve the puzzle!

# The Setup:
# First we need to create a cool list to store the data
#  Each element of this list is a list
#  Each element list has 5 values: the name, the 4 sides, and a list 
#   of the other puzzle pieces that this piece fits with 
#    I.E [(element list),...]
#         element list = [ funky_name, a, b, c, d, [pieces_that_fits_list]]
#         pieces_that_fits_list = [[connection(a)list],...,[connection(d)list]]
# This looks complex but the code will be simple (HOPEFULLY)

# This Version of the script will attempt to find all the solutions

# Rules of which side fits which side
puzzle_relation={}

# Basic list of puzzle piece profiles
puzzle_pieces=[]

# Advanced list of puzzle piece profiles
adv_puzzle_pieces=[]

# Iterative list
four_piece_potential=[]

# Solution List
solutions=[]

def create_adv_list():
    
    number_of_connections=0
    
    # Creates a adv_puzzle_piece for every puzzle piece
    for p_piece in puzzle_pieces:
        name = p_piece[0]
        side1 = p_piece[1][0]
        side2 = p_piece[1][1]
        side3 = p_piece[1][2]
        side4 = p_piece[1][3]
        connectionlist=[]
        
        # Create the connection list for p_piece
        for side_n in [side1,side2,side3,side4]:
            side_n_list=[]
            relatedpiece = puzzle_relation[side_n]
            
            # Looks at all the other puzzle pieces not of same name and 
            #  records them into the list if they fit with p_piece
            for puzzle_piece in puzzle_pieces:
                if puzzle_piece[0] != name:
                    for side in puzzle_piece[1]:
                        if side==relatedpiece:
                            side_n_list.append(puzzle_piece)
                            number_of_connections+=1
            connectionlist.append(side_n_list)
            
        # Append the adv_piece onto the adv list 
        adv_piece=[name,side1,side2,side3,side4,connectionlist]
        adv_puzzle_pieces.append(adv_piece)
    return number_of_connections/2

# Helper function that loops right from 1 to 4 based on a number line
def to_right(num):
    if num==4:
        return 1
    else:
        return num+1
 
# Helper function that loops left from 1 to 4 based on a number line  
def to_left(num):
    if num==1:
        return 4
    else:
        return num-1
    
    
# Creates a new puzzle piece with 4 of the smaller puzzle pieces

def create_four_pieces():
    
    # Loops though all the puzzle pieces and looks for 4 piece combination pieces
    for adv_piece in adv_puzzle_pieces:
        
        # Loops through all 4 sides of the adv_piece and looks for different combinations
        for num in range(1,5):
            
            # Sets the side of the puzzle piece (right side)
            side = adv_piece[num]
            # Sets the bottom of the puzzle piece
            bottom = adv_piece[to_right(num)]
            
            # Loops through all the pieces that can connect to the right side
            for right_piece in adv_piece[5][num]:
                # Loops through all the pieces that can connect to the bottom
                for bottom_piece in adv_piece[5][to_right(num)]:
                    
                    # Finds the list placement of side connection for the pieces that connect to the right side
                    right_piece_num=0
                    for j in range[1,5]:
                        if right_piece[j] != puzzle_relation[side]:
                            right_piece_num+=1
                    
                    # Finds the list placement of the bottom connection for the pieces that connect to the bottom side        
                    bottom_piece_num=0
                    for k in range[1,5]:
                        if bottom_piece[k] != puzzle_relation[bottom]:
                            bottom_piece_num+=1
                    
                    # Looks for a piece that fits into the bottom right side to complete the square
                    for bottom_right_piece in right_piece[5][to_left(right_piece_num)]:
                        for right_bottom_piece in bottom_piece[5][to_right(bottom_piece_num)]:
                            
                            # If such a piece exists, creates a new puzzle piece with the same structure as the pieces in puzzle relation
                            if bottom_right_piece == right_bottom_piece:
                                potential_four=[[[adv_piece[0],
                                                  bottom,side],
                                                 [right_piece[0],
                                                  right_piece[right_piece_num],
                                                  right_piece[to_left(right_piece_num)]]
                                                [bottom_piece_num[0],
                                                 bottom_piece[bottom_piece_num],
                                                 bottom_piece[to_right(bottom_piece_num)]]
                                                [right_bottom_piece[0]],
                                                puzzle_relation[bottom_piece[to_right(bottom_piece_num)]],
                                                puzzle_relation[right_piece[to_left(right_piece_num)]]],
                                                adv_piece[to_right(to_right(num))]+bottom_piece[to_right(to_right(bottom_piece_num))],
                                                adv_piece[to_left
                                four_piece_potential.append[potential]
    return 0
                                
def solve_puzzle():
    connection_num = create_adv_list()
    number_of_elements = len(puzzle_pieces)
    if connection_num < (2*number_of_elements**2 - 2*number_of_elements):
        return "no solution"
    create_four_pieces()
    for piece in four_piece_potential:
        used_pieces = []
        c_potential_solution=[]
        four_piece_possible = []
        
        for smaller_piece in piece:
            if smaller_piece[0] not in used_pieces:
                used_pieces.append(smaller_piece[0])
                four_piece_possible.append(piece)
                
                update_adv_puzzle_pieces()
                update_relation()
            
        if len(four_piece_possible) != 4:
            break
        puzzle_pieces = four_piece_possible
        update_adc_puzzle_pieces()
        update_puzzle_relation()
        
    if length(adv_puzzle_pieces)==1:
        return solution
    return solve_puzzle
    

# Gets the basic info for the puzzle through user input
def create_databank():
    
    # While loop continuation variables
    y=1
    x=1
    
    # Lets get the puzzle sides relationships
    print("Tell me the puzzle side relationship\nPlease only enter each relationship once!\n")
    while(y!=0):
        inserter=input("Name of the inserter:")
        accepter=input("\nName where the inserter fits into:")
        y=input("\nif no more relationships type 0, else type any other int")
        puzzle_relation[inserter] = accepter
        puzzle_relation[accepter] = inserter
    
    # Lets get the puzzle piece profiles
    print("make sure when you input sides you use consistent rotation!\n")
    while(x!=0):
        name=input("Funky puzzle piece name:")
        side1=input("\nFirst side:")
        side2=input("\nSide right of first side:")
        side3=input("\nSide right to previous side:")
        side4=input("\nSide right to previous side:")
        x=input("\nif no more pieces type 0, else type any other int")
        element=[name,[side1,side2,side3,side4]]
        puzzle_pieces.append(element)
    return solve_puzzle()
        
create_databank()