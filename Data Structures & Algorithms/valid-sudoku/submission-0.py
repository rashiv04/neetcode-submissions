class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                box_index=(r//3)*3+(c//3)
                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in box[box_index]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                box[box_index].add(value)
        return True
                