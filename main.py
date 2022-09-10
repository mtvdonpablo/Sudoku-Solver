board = [
    [7,8,"_",4,"_","_",1,2,"_"],
    [6,"_","_","_",7,5,"_","_",9],
    ["_","_","_",6,"_",1,"_",7,8],
    ["_","_",7,"_",4,"_",2,6,"_"],
    ["_","_",1,"_",5,"_",9,3,"_"],
    [9,"_",4,"_",6,"_","_","_",5],
    ["_",7,"_",3,"_","_","_",1,2],
    [1,2,"_","_","_",7,4,"_","_"],
    ["_",4,9,2,"_",6,"_","_",7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i , (row, col)):
            bo[row][col] = i 

            if solve(bo):
                return True
            bo[row][col] = "_"
    return False


#check if board/solution is valid
def valid(bo,num,pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1]!=i:
            return False
    #Check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    #Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3,box_y * 3 +3): 
        for j in range(box_x * 3,box_x * 3 +3): 
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 ==0 and i !=0:
            print("- - - - - - - - - - - -  ")
        for j in range(len(bo[0])):
            if j % 3 ==0 and j!=0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#print_board(board)

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]== "_": #if i replace 0s with _ or whatever to denote empty spaces change this
                return (i,j) # row,col
    return None 
                


print_board(board)
print("*************************************")
solve(board)
print_board(board)
