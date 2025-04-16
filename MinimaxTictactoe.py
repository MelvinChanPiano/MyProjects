def minimax(board, depth, maxi):
    outcome = evaluate(board)
    scores = []
    if outcome != 0:
        return outcome
    if not empty(board):
        return 0
   
    if maxi:
      mark = 'x'
    else:
      mark = 'o'

    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                board[row][col] = mark
                score = minimax(board, depth + 1, not maxi)
                scores.append(score)
                board[row][col] = '_'
   
    if maxi :
      return max(scores)
    else:
      return min(scores)

def evaluate(board):
    lines = []
    lines.extend(board)
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for l in lines:
        if l[0] == l[1] == l[2] and l[0] != '_':
            if l[0] == 'x':
              return 1
            else:
              return -1
    return 0

def empty(board):
    return any('_' in row for row in board)

def Thebest(board):
    Bscore = float('-inf')
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == '_':
                board[r][c] = 'x'
                score = minimax(board, 0, False)
                board[r][c] = '_'

                if score > Bscore:
                    Bscore = score
                    move = (r, c)
    return move

def output(board):
    print("\nCurrent board:")
    for row in board:
        print(" ".join(row))
    print("")

def gameover(board):
    score = evaluate(board)
    if score == 1:
        print("You lost.")
        return True
    elif score == -1:
        print("You win.")
        return True
    elif not empty(board):
        print("Draw.")
        return True
    return False

def main():
    board = [['_'] * 3 for _ in range(3)]
    print("Enter your moves (e.g. 2 1)")
    print("AI moves.")

    while True:
        output(board)
        aiMove = Thebest(board)
        if aiMove:
            board[aiMove[0]][aiMove[1]] = 'x'
            if gameover(board):
                output(board)
               
        output(board)

        while True:
            try:
                row, col = map(int, input("Your move (row col): ").split())
                if board[row][col] == '_':
                    board[row][col] = 'o'
                    break
                else:
                    print("Cell occupied, enter again: ")
            except:
                print("Invalid input. Enter two numbers between 0 and 2:")

        if gameover(board):
            output(board)
           
main()
