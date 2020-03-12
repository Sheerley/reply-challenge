
def fitness(board):
    totalTotalpotential = 0
    for rowInd,row in enumerate(board):
        for placeInd, place in enumerate(row):
            if place.kind == '#':
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
                totalTotalpotential += (workPotential + bonusPotential)
            else:
                print("we are screwed")
    return totalTotalpotential


def test_slice(m,i,j,slice_y = 3, slice_x = 3):
    sliceOfMatrix = [[m[a][b] for b in range(max(j-1,0), j + 2)] for a in range((i-1,0), i + 2)]
    return sliceOfMatrix

class worker():
    def __init__(self,kind,company,bonusPoints,potential,skills):
        self.kind = kind
        self.company = company
        self.skills = skills
        self.potential = potential
        self.workPotential = 0
        self.bonusPotential = 0 




