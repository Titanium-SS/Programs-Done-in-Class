def NQueens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def backtrack(board=[], row=0):
        if row == n:
            result.append(list(board))
            return
        for col in range(n):
            if is_valid(board, row, col):
                board.append(col)
                backtrack(board, row + 1)
                board.pop()

    result = []
    backtrack()
    
    return result


solution = NQueens(5)
print("Possible Solution Sets are: ")
cnt = 0
for one in solution:
    print(one)
    cnt+=1

print(f"Therefore, total no. of solutions are: {cnt}")
