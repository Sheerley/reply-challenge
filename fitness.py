def fitness(board):
    newBoard = []
    for rowInd,row in enumerate(board):
        for placeInd, place in enumerate(row):
            if place == '#':
                newBoard[rowInd][placeInd] = "#"
            elif(place == 'M'):
                pass     
            elif(place == "_"):
                ##creating submatrix
                submatrix = test_slice(board,rowInd,placeInd)
                
                ## skills update for given cell
                
            else:
                print("we are screwed")


def test_slice(m,i,j,slice_y = 3, slice_x = 3):
    sliceOfMatrix = [[m[a][b] for b in range(j, j + slice_x)] for a in range(i, i + slice_y)]
    return sliceOfMatrix


