def fitness(board):
    newBoard = []
    for rowInd,row in enumerate(board):
        for placeInd, place in enumerate(row):
            if place == '#':
                newBoard[rowInd][placeInd] = "#"
            elif(place.kind == 'M'):
                pass     
            elif(place.kind == "_"):
                ##creating submatrix
                submatrix = test_slice(board,rowInd,placeInd)
                ## skills update for given cell
                for rowsub in submatrix:
                    for placesub in rowsub:
                        calculatedSkillSum += placesub.skills
                
            else:
                print("we are screwed")


def test_slice(m,i,j,slice_y = 3, slice_x = 3):
    sliceOfMatrix = [[m[a][b] for b in range(j, j + slice_x)] for a in range(i, i + slice_y)]
    return sliceOfMatrix

class worker():
    def __init__(self,kind,company,bonusPoints,potential,skills):
        self.kind = kind
        self.company = company
        self.bonusPoints = bonusPoints
        self.skills = skills




