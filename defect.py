import numpy as np
from random import randrange

# Defects found per week with one person finding
WEEKS = [[10,5,8,25],
        [7,10,6,19],
        [6,5,5,16],
        [7,4,8,8],
        [2,5,2,14],
        [3,3,1,16],
        [1,2,1,15],
        [3,1,3,9],
        [1,4,1,7],
        [0,2,3,5],
        [1,1,1,5],
        [1,1,4,3],
        [2,0,3,2],
        [2,1,2,2],
        [1,1,0,1],
        [0,0,1,1],
        [2,2,0,0],
        [0,1,0,1],
        [1,2,0,1],
        [0,0,1,0]]

# Defects found per week with everyone finding 
# and progressively moved to fixing
MOVED_WEEKS = [[23,20,19,60],
        [9,9,10,22],
        [4,5,2,31],
        [3,1,3,9],
        [1,4,1,7],
        [0,2,3,5],
        [1,1,1,5],
        [1,1,4,3],
        [2,0,3,2],
        [2,1,2,2],
        [1,1,0,1],
        [0,0,1,1],
        [2,2,0,0],
        [0,1,0,1],
        [1,2,0,1],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,1,0],
        [0,1,0,0],
        [0,0,0,1]]

# 2 people working 25 hour weeks
HOURS = 50

def easy_first(hours_remaining, defects):

    while hours_remaining > 0:

        if defects[2] > 0 and hours_remaining >= 2: # Easy, Major
            hours_remaining -= 2
            defects[2] -= 1

        elif defects[3] > 0 and hours_remaining >= 2: # Easy, Minor
            hours_remaining -= 2
            defects[3] -= 1

        elif defects[0] > 0 and hours_remaining >= 5: # Hard, Major
            hours_remaining -= 5
            defects[0] -= 1

        elif defects[1] > 0 and hours_remaining >= 5: # Hard, Minor
            hours_remaining -= 5
            defects[1] -= 1

        else: # No defects left
            break
    
    return defects

def hard_first(hours_remaining, defects):

    while hours_remaining > 0:

        if defects[0] > 0 and hours_remaining >= 5: # Hard, Major
            hours_remaining -= 5
            defects[0] -= 1

        elif defects[1] > 0 and hours_remaining >= 5: # Hard, Minor
            hours_remaining -= 5
            defects[1] -= 1

        elif defects[2] > 0 and hours_remaining >= 2: # Easy, Major
            hours_remaining -= 2
            defects[2] -= 1

        elif defects[3] > 0 and hours_remaining >= 2: # Easy, Minor
            hours_remaining -= 2
            defects[3] -= 1

        else: # No defects left
            break
            
    return defects

def major_first(hours_remaining, defects):

    while hours_remaining > 0:

        if defects[2] > 0 and hours_remaining >= 2: # Easy, Major
            hours_remaining -= 2
            defects[2] -= 1

        elif defects[0] > 0 and hours_remaining >= 5: # Hard, Major
            hours_remaining -= 5
            defects[0] -= 1

        elif defects[3] > 0 and hours_remaining >= 2: # Easy, Minor
            hours_remaining -= 2
            defects[3] -= 1

        elif defects[1] > 0 and hours_remaining >= 5: # Hard, Minor
            hours_remaining -= 5
            defects[1] -= 1

        else: # No defects left
            break
            
    return defects

def minor_first(hours_remaining, defects):

    while hours_remaining > 0:

        if defects[3] > 0 and hours_remaining >= 2: # Easy, Minor
            hours_remaining -= 2
            defects[3] -= 1

        elif defects[1] > 0 and hours_remaining >= 5: # Hard, Minor
            hours_remaining -= 5
            defects[1] -= 1

        elif defects[2] > 0 and hours_remaining >= 2: # Easy, Major
            hours_remaining -= 2
            defects[2] -= 1

        elif defects[0] > 0 and hours_remaining >= 5: # Hard, Major
            hours_remaining -= 5
            defects[0] -= 1

        else: # No defects left
            break
            
    return defects

def random_first(hours_remaining, defects):

    while hours_remaining >= 2:

        index = randrange(4)

        if index == 0 and defects[0] > 0 and hours_remaining >= 5: # Hard, Major
            hours_remaining -= 5
            defects[0] -= 1

        elif index == 1 and defects[1] > 0 and hours_remaining >= 5: # Hard, Minor
            hours_remaining -= 5
            defects[1] -= 1

        elif index == 2 and defects[2] > 0 and hours_remaining >= 2: # Easy, Major
            hours_remaining -= 2
            defects[2] -= 1

        elif index == 3 and defects[3] > 0 and hours_remaining >= 2: # Easy, Minor
            hours_remaining -= 2
            defects[3] -= 1

        elif sum(defects) == 0: # No defects left
            break
            
    return defects

def found_first():

    defects = [0,0,0,0]
    weeks = WEEKS.copy()
    defect_tracker = np.zeros(shape=(20,4))

    for i in range(0,20):
        hours_remaining = HOURS
        defects = [sum(x) for x in zip(defects, WEEKS[i])]

        for j in range(0, i+1):

            if sum(weeks[j]) == 0:
                continue

            while hours_remaining >= 2:

                index = randrange(4)

                if index == 0 and weeks[j][0] > 0 and hours_remaining >= 5: # Hard, Major
                    hours_remaining -= 5
                    defects[0] -= 1
                    weeks[j][0] -= 1

                elif index == 1 and weeks[j][1] > 0 and hours_remaining >= 5: # Hard, Minor
                    hours_remaining -= 5
                    defects[1] -= 1
                    weeks[j][1] -= 1

                elif index == 2 and weeks[j][2] > 0 and hours_remaining >= 2: # Easy, Major
                    hours_remaining -= 2
                    defects[2] -= 1
                    weeks[j][2] -= 1

                elif index == 3 and weeks[j][3] > 0 and hours_remaining >= 2: # Easy, Minor
                    hours_remaining -= 2
                    defects[3] -= 1
                    weeks[j][3] -= 1

                elif sum(weeks[j]) == 0: # No defects left
                    break

        defect_tracker[i] = defects
            
    defect_tracker = defect_tracker.astype(int)
    np.savetxt('found.csv', defect_tracker, delimiter=',')

def half_staff():

    defects = [52,52,52,151]
    defect_tracker = np.zeros(shape=(10,4))

    for i in range(0,10):
        hours_remaining = 75
        defects = major_first(hours_remaining, defects)
        defect_tracker[i] = defects
            
    defect_tracker = defect_tracker.astype(int)
    np.savetxt('half_staff.csv', defect_tracker, delimiter=',')

def moved_staff():

    defects = [0,0,0,0]
    defect_tracker = np.zeros(shape=(20,4))

    for i in range(0,1):
        defects = [sum(x) for x in zip(defects, MOVED_WEEKS[i])]
        hours_remaining = 0 * 25 #No fixers
        defects = major_first(hours_remaining, defects)
        defect_tracker[i] = defects

    for i in range(1,3):
        defects = [sum(x) for x in zip(defects, MOVED_WEEKS[i])]
        hours_remaining = 1 * 25 #One fixer
        defects = major_first(hours_remaining, defects)
        defect_tracker[i] = defects

    for i in range(3,20):
        defects = [sum(x) for x in zip(defects, MOVED_WEEKS[i])]
        hours_remaining = 2 * 25 #Two fixers
        defects = major_first(hours_remaining, defects)
        defect_tracker[i] = defects

    defect_tracker = defect_tracker.astype(int)
    np.savetxt('moved_staff.csv', defect_tracker, delimiter=',')


if __name__== "__main__":
    moved_staff()
    # defects = [0,0,0,0]
    # defect_tracker = np.zeros(shape=(20,4))

    # for i in range(0,20):
    #     defects = [sum(x) for x in zip(defects, WEEKS[i])]
    #     defects = random_first(HOURS, defects)
    #     defect_tracker[i] = defects

    # defect_tracker = defect_tracker.astype(int)
    # np.savetxt('random.csv', defect_tracker, delimiter=',')
