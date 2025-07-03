class Connect4App:

    def __init__(self):
        self.centerPoint = ([65,490], [125,490], [185,490], [245,490], [305,490], [365,490], [425,490])
        self.count = [0,0,0,0,0,0,0]
        self.row = [5,5,5,5,5,5,5]
        self.player1, self.player2 = True, False
        self.total = 0
        self.board =[
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ']
        ]

    def run(self, interface):
        self.interface = interface
        while True:
            if self.player1:
                self.interface.updatePlayerTurn('Player 1', 'red')
            else:
                self.interface.updatePlayerTurn('Player 2', 'yellow3')
            column = self.interface.ButtonClicked()
            if self.count[column] != 6:
                if self.player1:
                    self.interface.drawToken(self.centerPoint[column], 'red')
                    self.board[self.row[column]][column] = 'r'
                else:
                    self.interface.drawToken(self.centerPoint[column], 'yellow')
                    self.board[self.row[column]][column] = 'y'
                self.centerPoint[column][1] = self.centerPoint[column][1] - 75
                self.row[column] = self.row[column] - 1
                self.count[column] = self.count[column] + 1
                self.total = self.total + 1
                self.player1, self.player2 = self.player2, self.player1
            if self.total == 42:
                self.interface.updateResult('Tie')
                break
            else:
                result = self.checkDiagonal()
                if result:
                    self.interface.updateResult(result)
                    break
                else:
                    result = self.checkHorizontal()
                    if result:
                        self.interface.updateResult(result)
                        break
                    else:
                        result = self.checkVertical()
                        if result:
                            self.interface.updateResult(result)
                            break

    def checkHorizontal(self):
        for i in self.board:
            row = ",".join(i)
            if 'r,r,r,r' in row:
                return 'Player 1'
            elif 'y,y,y,y' in row:
                return 'Player 2'

    def checkVertical(self):
        for n in range(7):
            column = ''
            for i in range(len(self.board)):
                column = column + self.board[i][n]
            if 'rrrr' in column:
                return 'Player 1'
            elif 'yyyy' in column:
                return 'Player 2'

    def checkDiagonal(self):
        coords = ((0,3), (0,4), (0,5), (1,5), (2,5), (3,5))
        for i in range(len(coords)):
            diagonal = ''
            x, y = coords[i][0], coords[i][1]
            if i == 4 or i == 5:
                while x != 7:
                    diagonal = diagonal + self.board[y][x]
                    y = y - 1
                    x = x + 1
            else:
                while y != -1:
                    diagonal = diagonal + self.board[y][x]
                    y = y - 1
                    x = x + 1
            if 'rrrr' in diagonal:
                return 'Player 1'
            elif 'yyyy' in diagonal:
                return 'Player 2'
        coords = ((6,3), (6,4), (6,5), (5,5), (4,5), (3,5))
        for i in range(len(coords)):
            diagonal = ''
            x, y = coords[i][0], coords[i][1]
            if i == 4 or i == 5:
                while x != -1:
                    diagonal = diagonal + self.board[y][x]
                    y = y - 1
                    x = x - 1
            else:
                while y != -1:
                    diagonal = diagonal + self.board[y][x]
                    y = y - 1
                    x = x - 1
            if 'rrrr' in diagonal:
                return 'Player 1'
            elif 'yyyy' in diagonal:
                return 'Player 2'
        return False
