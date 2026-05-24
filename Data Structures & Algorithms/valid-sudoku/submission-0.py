class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        number_set = set()
        for  fila in board:
            for elemento in fila:
                if elemento in number_set:
                    return False
                elif elemento != ".":
                    number_set.add(elemento)
            number_set.clear()
        
        filas = len(board)
        columnas = len(board[0])

        for c in range(columnas):
            for f in range(filas):
                elemento = board[f][c]
                if elemento != ".":
                    if elemento in number_set:
                        return False
                    number_set.add(elemento)
            number_set.clear()

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        elemento = board[r + i][c + j]
                        if elemento != ".":
                            if elemento in number_set:
                                return False
                            number_set.add(elemento)
                number_set.clear()
        
        return True
