"""
Author  : Abhishek Nikkudala
Date    : 05/02/2019
Version : Python 2.7
Steps   :
    1. Find the effective input 
        a) Number of Horizontal flips
        b) number of Vertical flips
        c) Effective shift for an integer input
    2. Build the board
    3. Return the desired output
"""

"""
Traverse the input,
Calculate the effective shift from the inputs and count of flips.

Counting Mechanism : 
    1. Push key if not in dictionary.
    2. Pop if already present in the dictionary.
    3. Steps 1,2 indicate if the board has to be flipped H/V or both. 

Sample output : 
input = ['H','V',-5,'H',2,'V','V','H']
effectiveShift = -3 
flipDict = {'h': 1, 'v': 1}
"""
def findEffectiveInput(inputList):  
    effectiveShift = 0
    flipDict = {}      
    for item in inputList:
        if type(item) == int:
            effectiveShift += item
        else:
            if item.lower() in flipDict.keys():
                flipDict.pop(item.lower())
            else:
                flipDict[item.lower()] = 1
    return effectiveShift,flipDict

"""
The function flips the board around the center,
It takes the board layout as
input and returns the mirror image.
"""
def verticalShift(board):    
    verticalShiftedBoard = []
    columnLength = len(board) 
    for row in range(len(board)):
        tempList = []
        for column in range(len(board[row])):
            tempList.append(board[columnLength - row - 1][column])
        verticalShiftedBoard.append(tempList)
    return verticalShiftedBoard

"""
The function generates a mirror image, 
It takes the board layout as
input and returns the mirror image.
"""
def horizontalShift(board):
    horizontalShiftedBoard = []

    # Omitting the use of reverse function, that's an alternative.
    for row in range(len(board)):
        tempList = []
        rowLength = len(board[row]) 
        for column in range(rowLength):
            tempList.append(board[row][rowLength - column - 1])
        horizontalShiftedBoard.append(tempList)
    return horizontalShiftedBoard

"""
Slide function works assuming the keys in row are arranged in circular manner.
Assumption : The row in a board is arranged in circular manner.
"""
def slide(board, shiftIndicator):
    slideBoard = []

    for row in range(len(board)):
        tempList = []
        rowLength = len(board[row]) 
        for column in range(len(board[row])):
            # Calculating the effective length, ensuring the list is 
            # never out of bound, Functions in circular manner.
            tempList.append(board[row][(column + shiftIndicator) % rowLength])
        slideBoard.append(tempList)
    return slideBoard

"""
The function is to rearrange the board based in the 
input parameters, the function returns updated board.
"""
def rearrangeBoard(board,shiftindicator,flipDict):
    if 'h' in flipDict.keys():
        board = horizontalShift(board)
    
    if 'v' in flipDict.keys():
        board = verticalShift(board)

    board = slide(board, shiftindicator)
    return board

"""
The function generates a dictionary which serves as lookup,
The function takes board as input and returns dictionary.

Sample Output: dict = {'v' : 1.2}
"""
def generateMappingDict(board):
    mapBoard = {}
    for row in range(len(board)):
        for column in range(len(board[row])):
            mapBoard[board[row][column]] = str(row)+ '.' + str(column)                  
    return mapBoard

"""
The function generates a dictionary which serves as lookup,
The function takes board as input and returns dictionary.

Sample Output: dict = {'1.2' : 'v'}
"""
def generatekeyValuePairs(board):
    mapBoard = {}
    for row in range(len(board)):
        for column in range(len(board[row])):
            #mapBoard[board[row][column]] = str(row)+ '.' + str(column)
            mapBoard[str(row)+ '.' + str(column)] = board[row][column]
    #print mapBoard                        
    return mapBoard


def main():
    # ------------------------------------------------- #
    # Configure Inputs
    inputList = ['H','V',-5,'H',2,'V','V','H']
    board = [
        [1,2,3,4,5,6,7,8,9,0],
        ['q','w','e','r','t','y','u','i','o','p'],
        ['a','s','d','f','g','h','j','k','l',';'],
        ['z','x','c','v','b','n','m',',','.','/']
    ]
    inputStream = 'qw'
    
    # ------------------------------------------------- #

    shiftIndicator,flipDict = findEffectiveInput(inputList)   
    finalBoard = rearrangeBoard(board,shiftIndicator,flipDict) 
    mapDict = generateMappingDict(board)
    finalMapDict = generateMappingDict(finalBoard)
    outputStream = ''


    OptimisedfinalMapDict = generatekeyValuePairs(finalBoard)

    for char in inputStream:
        if char not in mapDict.keys():
            # If character is not present in the keyboard,
            # skip the character, Pass it untransformed.
            outputStream += str(char)
        else :
            # Approach 1 : nested for loops with o(n^2) complexity
            """
            for item in finalMapDict.values():
                # Traverse list once to find a match with input stream
                # If found, Append it to the output.
                if mapDict[char] == item:
                    finalRow = int(item.split('.')[0])
                    finalColumn =  int(item.split('.')[1])
                    outputStream += finalBoard[finalRow][finalColumn]
            """

            # Approach 2 : Simple Lookup with O(1) complexity
            outputStream += OptimisedfinalMapDict[mapDict[char]]          

    print outputStream

# Calling the main method  
if __name__ == "__main__": 
    main()