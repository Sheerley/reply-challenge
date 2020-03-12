
def fitness(board):
    for rowInd,row in enumerate(board):
        for placeInd, place in enumerate(row):
            if place == '#':
                pass
            elif(place.kind == 'M'):
                pass     
            elif(place.kind == "_"):
                ##creating submatrix
                submatrix = test_slice(board,rowInd,placeInd)
                ## skills update for given cell
                bonusPotential = 0
                workPotential = 0
                for rowsub in submatrix:
                    for placesub in rowsub:
                        if(rowsub != 2 and placesub != 2):
                            pass
                        else:
                            if placesub.company == place.company:
                                bonusPotential += placesub.potential*(place.potential)
                            if placesub.kind == '_':
                                skill_sum = place.skills + placesub.kind
                                skill_sum = list( dict.fromkeys(skill_sum))
                                skill_difference  = [x for x in skill_sum if x not in place.skills]
                                workPotential += len(skill_difference) * (len(skill_sum) - len(skill_difference))
                place.workPotential = workPotential
                place.bonusPotential = bonusPotential
            else:
                print("we are screwed")


def test_slice(m,i,j,slice_y = 3, slice_x = 3):
    sliceOfMatrix = [[m[a][b] for b in range(j, j + slice_x)] for a in range(i, i + slice_y)]
    return sliceOfMatrix

class worker():
    def __init__(self,kind,company,bonusPoints,potential,skills):
        self.kind = kind
        self.company = company
        self.skills = skills
        self.potential = potential
        self.workPotential = 0
        self.bonusPotential = 0 




