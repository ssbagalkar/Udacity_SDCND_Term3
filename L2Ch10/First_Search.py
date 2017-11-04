import math
#  ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
rowIdx = init[0]
colIdx = init[1]

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    rowIdx = init[0]
    colIdx = init[1]
    xLimitStart = 0
    yLimitStart = 0
    xLimitEnd = len(grid) -1
    yLimitEnd = len(grid[0]) -1
    visited = [[0,0]]
    checked = []
    currentNodes=[]
    newOpenList=[]
    isContinue = True
    isWay = True

    while (isContinue):

        # search in all 4 directions of current node
        for ii in range(0,4):
            currentX = rowIdx + delta[ii][0]
            currentY = colIdx + delta[ii][1]

            # Check if the row and col indexes are within bounds
            if ((currentX >= xLimitStart ) and (currentX <= xLimitEnd) and (currentY >= yLimitStart) and (currentY <= yLimitEnd)):

                if (grid[currentX][currentY] != 1):

                    if ([currentX,currentY] not in visited):

                        if ( [currentX,currentY] not in currentNodes):

                            currentNodes.append([currentX,currentY])


        if not currentNodes:
            isContinue = False
            isWay  = False
            print("fail")

        if isWay:
            print("new open list:")
            maxCost = math.inf
            for ii in range(0,len(currentNodes)):
                if currentNodes[ii] not in checked:
                    # put in checked
                    checked.extend([currentNodes[ii]])

                    # put in  newOpenList and add cost
                    addPointsX = currentNodes[ii][0]
                    addPointsY = currentNodes[ii][1]
                    newOpenList.extend([[addPointsX,addPointsY]])

                    #append to new open list
                    indexOfnewOpenList = len(newOpenList)-1
                    newOpenList[indexOfnewOpenList].insert(0,cost)


                print(newOpenList[ii])
                if(newOpenList[ii][0] <= maxCost):
                    maxCost = newOpenList[ii][0]
                    indexToBeRemoved = ii

            # Remove that index for  the newOpenList
            print("take list item :")
            print(newOpenList[indexToBeRemoved])

            # put this is visited
            visited.append(newOpenList[indexToBeRemoved][1:3])

            cost = newOpenList[indexToBeRemoved][0]

            #Update rowIndex and colIndex
            rowIdx = newOpenList[indexToBeRemoved][1]
            colIdx = newOpenList[indexToBeRemoved][2]

            # now delete from newOpenList and currentNodes
            del newOpenList[indexToBeRemoved]
            del currentNodes[indexToBeRemoved]

            # Increase cost
            cost = cost + 1

            # Stopping criteria
            if ( (rowIdx == goal[0]) and (colIdx == goal[1]) ) :
                isContinue=False
                print("Goal Reached !!")
    path =0
    return path

path = search(grid,init,goal,cost)
