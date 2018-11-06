class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    wordMatrix = None
    matrixCol = None
    matrixRow = None
    
    def __init__(self, puzzle):
        self.matrixCol = len(puzzle[0])
        self.matrixRow = len(puzzle)

        self.wordMatrix = [[]*self.matrixRow for x in range(self.matrixCol)]

        for i in range(0, self.matrixRow-1):
            for j in range(0, self.matrixCol-1):
                self.wordMatrix[i][j] = 1

    def search(self, word):
        pass

puzzle = ['jefblpepre',
                  'camdcimgtc',
                  'oivokprjsm',
                  'pbwasqroua',
                  'rixilelhrs',
                  'wolcqlirpc',
                  'fortranftw',
                  'alxhpburyi',
                  'clojurermt',
                  'jalaycalmp']
a =  WordSearch(puzzle)
print(a.wordMatrix)
print(a.matrixCol)
print(a.matrixRow)
