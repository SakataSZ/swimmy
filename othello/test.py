SPACE = 0  # 何も置かれていない
BLACK = 1  # 黒
WHITE = 2  # 白
OUT = -1  # 盤面の外(番兵)
SIZE = 10  # 盤面の大きさ

# プレイヤーを表す数値を文字列に変換する為の辞書
PLAYER = {BLACK: "黒", WHITE: "白"}
BOARD = {BLACK: "●", WHITE: "○", SPACE: "□"}


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
    while True:
        print(PLAYER[player] + "の番です")
        move = input("指し手を入力してください : ")
        move = move.split(' ')
        if len(move) == 2:
            i = move[0]
            j = move[1]
            if i.isdecimal() and j.isdecimal():
                i = int(i)
                j = int(j)
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


def bi_check(board, player, j, dj):
    look = 1
    while board[j + dj * look] == opp(player):
        look += 1
    if board[j + dj * look] == player:
        return look - 1
    else:
        return 0


def test():
    player = WHITE
    board = [-1, 0, 2, 2, 1, 0, 0, 0, 0, -1]
    j = 5
    dj = -1

    print(bi_check(board, player, j, dj))


def count_turn_over(board, player, i, j, di, dj):
    view = 1
    while board[i + view * di][j + view * dj] == opp(player):
        view += 1

    if board[i + view * di][j + view * dj] == player:
        return view - 1
    else:
        return 0


def is_legal_move(board, player, i, j):
    if board[i][j] is not SPACE:
        return False

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if count_turn_over(board, player, i, j, di, dj):
                return True

    return False


def set_and_turn_over(board, player, i, j):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            count = count_turn_over(board, player, i, j, di, dj)
            for c in range(count + 1):
                board[i + c * di][j + c * dj] = player

    board[i][j] = player


def exit_legal_move(board, player):
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            if is_legal_move(board, player, i, j):
                return True

    return False


def show_winner(board):
    cnt = {BLACK: 0, WHITE: 0, SPACE: 0}
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            cnt[board[i][j]] += 1

    print('#' * 15)
    print("黒 : {}, 白 : {}".format(cnt[BLACK], cnt[WHITE]))
    print("{}の勝利".format("黒" if cnt[WHITE] < cnt[BLACK] else "白"))
    print('#' * 15)


def show_board_cui(board):
    print()
    print("{:1s}".format(''), end='')
    for n in range(1, SIZE - 1):
        print("{:3d}".format(n), end='')
    print()
    for i in range(1, SIZE - 1):
        print("{:<3d}".format(i), end='')
        for j in range(1, SIZE - 1):
            print("{:3s}".format(BOARD[board[i][j]]), end='')
        print()
    print()


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board_cui(board)
        if not exit_legal_move(board, player):
            print(PLAYER[player] + "石を置ける場所がありません. パスします")
            player = opp(player)
            if not exit_legal_move(board, player):
                print(PLAYER[player] + "石を置ける場所がありません. ゲームを終了します")
                show_winner(board)
                break

        i, j = get_move(player)
        if is_legal_move(board, player, i, j):
            set_and_turn_over(board, player, i, j)
            player = opp(player)
        else:
            print("石を置けません")


if __name__ == "__main__":
    main()
