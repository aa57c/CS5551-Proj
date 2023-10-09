class Board:
    positions = []
    plr_turn = 0
    active_mills = []
    remaining_turns = 0
    permissible_moves = {}

    def __init__(self):
        self.positions = [0 for _ in range(24)]
        self.plr_turn = 1
        self.active_mills = []
        self.remaining_turns = 18
        self.permissible_moves = {
            0: [1, 3], 1: [0, 2, 9], 2: [1, 4], 3: [0, 11, 5], 4: [2, 12, 7],
            5: [3, 6], 6: [5, 7, 14], 7: [4, 6], 8: [9, 11], 9: [1, 8, 17, 10],
            10: [9, 12], 11: [8, 3, 19, 13], 12: [20, 10, 4, 15], 13: [11, 14],
            14: [13, 22, 6, 15], 15: [14, 12], 16: [19, 17], 17: [16, 18, 9],
            18: [17, 20], 19: [16, 11, 21], 20: [18, 12, 23], 21: [19, 22],
            22: [14, 21, 23], 23: [20, 22]
        }

    def getBoardPositions(self):
        return self.positions
    
    def getPlayerTurn(self):
        return self.plr_turn
    
    def getActiveMills(self):
        return self.active_mills
    
    def getRemainingTurns(self):
        return self.remaining_turns
    
    def getPermissibleMoves(self):
        return self.permissible_moves
    
    def setBoardPositions(self, positions):
        self.positions = positions
    
    def setPlrTurn(self, turn):
        self.plr_turn = turn
    
    def setActiveMills(self, active_mills):
        self.active_mills = active_mills
    
    def setRemainingTurns(self, rem_turns):
        self.remaining_turns = rem_turns

    def setPermissibleMoves(self, perm_moves):
        self.permissible_moves = perm_moves
    



    

    

    




