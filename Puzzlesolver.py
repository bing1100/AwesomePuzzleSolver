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

# Rules of which side fits which side
puzzle_relation={}

# Basic list of puzzle piece profiles
puzzle_pieces=[]

# Advanced list of puzzle piece profiles
adv_puzzle_pieces=[]

def create_adv_list():
    
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
                            side_n_list.append(puzzle_piece[0])
            connectionlist.append(side_n_list)
            
        # Append the adv_piece onto the adv list 
        adv_piece=[name,side1,side2,side3,side4,connectionlist]
        adv_puzzle_pieces.append(adv_piece)
    return 0

def solve_puzzle():
    create_adv_list()
    solution=[]
    for
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