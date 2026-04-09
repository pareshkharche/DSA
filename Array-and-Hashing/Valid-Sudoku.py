#Valid Sodoku

from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=defaultdict(set)
        rows=defaultdict(set)
        squares=defaultdict(set) #r//3, c//3
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
            
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
                
        return True

board =[["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

# board=[["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]
sol= Solution()
print(sol.isValidSudoku(board))

#TC:O(1)  SC:O(n) or in generalized case O(n^2)



class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create sets to keep track of seen numbers for rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Ignore empty cells
                if val == ".":
                    continue

                # 1. Check the current row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # 2. Check the current column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # 3. Check the current 3x3 sub-box
                # Formula to find the box index: (row // 3) * 3 + (col // 3)
                box_idx = (r // 3) * 3 + (c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)

        return True

