SPACE = 0   # 何も置かれていない
BLACK = 1   # 黒
WHITE = 2   # 白
OUT = -1    # 盤面の外(番兵)
SIZE = 10   # 盤面の大きさ
PLAYER = {BLACK: "黒", WHITE: "白"}


def show_array(board):
    for i in range(SIZE):
        for j in range(SIZE):
            print("{:3d}".format(board[i][j]), end='')
        print()


def init_board(board):
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            board[i][j] = SPACE

    board[4][4] = WHITE
    board[5][5] = WHITE
    board[4][5] = BLACK
    board[5][4] = BLACK


def show_board(board):
    print()
    print("{:5s}".format(''), end='')
    for n in range(1, SIZE - 1):
        print("{:3d}".format(n), end='')
    print()
    for i in range(SIZE):
        if i == 0 or i == 9:
            print("{:2s}".format(''), end='')
        else:
            print("{:<2d}".format(i), end='')

        for j in range(SIZE):
            print("{:3d}".format(board[i][j]), end='')
        print()
    print()


def get_move(player):
    # 正しい形式で入力されるまで繰り返す
    while True:
        print(PLAYER[player] + "の番です")
        move = input("指し手を入力してください : ")
        move = move.split(' ')
        # 2つの文字がスペース区切りで入力されているか
        if len(move) == 2:
            i = move[0]
            j = move[1]
            # 2つの文字が数字か
            if i.isdecimal() and j.isdecimal():
                i = int(i)      # 数値に変換
                j = int(j)      # 数値に変換
                # 2つの数値が盤面に収まる値か
                if 1 <= i <= 8 and 1 <= j <= 8:
                    return [i, j]
        print("正しい形式で入力して下さい\n")


def opp(player):
    return 3 - player


def check(board, player, j):
    look = 1
    while board[j + look] == opp(player):
        look += 1
    if board[j + look] == player:
        return look - 1
    else:
        return 0


def test():
    player = BLACK
    board = [-1, 0, 2, 2, 1, 0, 0, 0, 0, -1]
    j = 1

    print(check(board, player, j))


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board(board)
        i, j = get_move(player)
        board[i][j] = player
        player = opp(player)


if __name__ == "__main__":
    test()
