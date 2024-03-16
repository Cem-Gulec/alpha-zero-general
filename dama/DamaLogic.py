class Board:
    def __init__(self, n = 8):
        "Set up initial board configuration."

        self.n = n
        # Create the empty board array.
        self.pieces = []
        for i in range(self.n):
            self.pieces.append([0] * self.n)

        # positif: beyaz
        # negatif: siyah
        # ilk başta: -1, +1
        # ilk hamle yaptıktan sonra -2, +2
            
        # hem taşlar hem oyuncular ("player") için durum aynı
        self.pieces[0]  = [-1] * self.n
        self.pieces[1]  = [-1] * self.n
        self.pieces[-2] = [1] * self.n
        self.pieces[-1] = [1] * self.n
        
        # self.pieces[3][3] = -1
        # self.pieces[4][3] = 1
    
    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]
    
    # playera şimdilik ihtiyaç yok zaten hallediyoruz
    def execute_move(self, move, player):
        c = (move[0], move[1])
        t = (move[2], move[3])
        cx, cy = c
        tx, ty = t

        self[tx][ty] = self[cx][cy]
        self[cx][cy] = 0
    
    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black
        """
        color_map = {-2: -1, -1: -1, 1: 1, 2: 1, 0: 0}
        moves = []  # stores the legal moves.

        # Get all the squares with pieces of the given color.
        for y in range(self.n):
            for x in range(self.n):
                if color_map[self[x][y]] == color:
                    newmoves = self.get_moves_for_square((x,y))
                    for i in newmoves:
                        moves.append(i)
        return list(moves)
    
    def get_moves_for_square(self, square):
        """Returns all the legal moves that use the given square as a base.
        That is, if the given square is (3,4) and it contains a black piece,
        and (3,5) and (3,6) contain white pieces, and (3,7) is empty, one
        of the returned moves is (3,7) because everything from there to (3,4)
        is flipped.
        """
        # returns a list of moves
        actions_for_a_piece = []
        row, col = square
        rules = {2: [(-1, 0), (-1, -1), (-1, 1)], 
                 1: [(-1, 0), (-2, 0), (-1, -1), (-1, 1)],
                -2: [(1, 0), (1, 1), (1, -1)], 
                -1: [(1, 0), (2, 0), (1, 1), (1, -1)]}
        
        for row_oper, col_oper in rules[self.pieces[row][col]]:
            target_row, target_col = (row + row_oper, col + col_oper)
            action = [row, col, target_row, target_col]
            if self.is_legal_action(action):
                actions_for_a_piece.append(action)

        return actions_for_a_piece
    
    def is_legal_action(self, action):
        check_colors = {-2: "black", -1: "black", 1: "white", 2: "white", "white": -1, "black": 1}
        current_pos = (action[0], action[1])
        target_pos  = (action[2], action[3])
        row, col = current_pos
        target_row, target_col = target_pos
        if target_row < 0 or target_row >= self.n or target_col < 0 or target_col >= self.n:
            return False
        if col != target_col and self.pieces[target_row][target_col] == 0:
            return False
        if col != target_col and check_colors[self.pieces[row][col]] == check_colors[self.pieces[target_row][target_col]]:
            return False
        oper = check_colors[check_colors[self.pieces[row][col]]]
        if col == target_col and self.pieces[target_row][target_col] != 0:
            return False
        if col == target_col and self.pieces[row + oper][col] != 0:
            return False

        return True

    def is_game_over(self, player):
        check = True
        temp = {1: 0, -1: self.n - 1}
        temp2 = {-1: -2, 1: 2}
        temp3 = {1: [-1, -2], -1: [1, 2]}

        is_game_over = temp2[player] in self.pieces[temp[player]]
        if is_game_over:
            return 1
         
        for row in self.pieces:
            for piece in row:
                if piece in temp3[player]:
                    check = False

        if check:
            return 1
        
        check = True
        temp_player = -player

        is_game_over = temp2[temp_player] in self.pieces[temp[temp_player]]
        if is_game_over:
            return -1
         
        for row in self.pieces:
            for piece in row:
                if piece in temp3[temp_player]:
                    check = False

        if check:
            return -1

        no_move_for_first_user = len(self.get_legal_moves(player)) == 0
        temp_player = -player
        no_move_for_second_user = len(self.get_legal_moves(temp_player)) == 0
    
        if no_move_for_first_user and no_move_for_second_user:
            return 1e-4

        # hamle sırası kimdeyse hamlesi yoksa
        elif no_move_for_first_user:
            return 1e-4

        return 0       
    
# x = Dama(8)
# print(x.getInitBoard())
# print(x.getGameEnded(x.getInitBoard(), -1))