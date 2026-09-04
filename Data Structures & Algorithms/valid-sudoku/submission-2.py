class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                square = (row//3, col//3)
                if num == ".":
                    continue
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in squares[square]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                squares[square].add(num)
        return True
                        