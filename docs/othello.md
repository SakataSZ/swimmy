---
title: オセロの作成
---

# 1. 二次元配列

## 1.1 二次元配列とは

以下のようなデータ構造を二次元配列と呼びます.

|     | 0          | 1          | 2          |
|-----|------------|------------|------------|
| 0   | data[0][0] | data[0][1] | data[0][2] |
| 1   | data[1][0] | data[1][1] | data[1][2] |
| 2   | data[2][0] | data[2][1] | data[2][2] |

変数はデータを格納する箱のようなものでしたね.

```python
data = 1
```

配列は変数が1列に並んだデータ構造です.

```python
data = [1, 2, 3]
```

そして二次元配列は配列が並んでいるようなデータ構造です.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

> 二次元配列を用いることでオセロの盤面を簡単に表現できます.
> ゲーム制作や画像処理など様々な場面で使用されます.

## 1.2 二次元配列の生成とアクセス

以下のように宣言することで二次元配列が生成されます.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

|     | 0   | 1   | 2   |
|-----|-----|-----|-----|
| 0   | 1   | 2   | 3   |
| 1   | 4   | 5   | 6   |
| 2   | 7   | 8   | 9   |

1行目の2列目の内容を出力したい時は以下のようにします.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(data[0][1])
```

出力結果は以下のようになります.

```
2
```

二次元配列は`data[行][列]`のような形で添え字を指定することでアクセスできます.

1行目の3列目に値を代入したい場合は以下のようにします.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

data[0][2] = 30
```

|     | 0   | 1   | 2   |
|-----|-----|-----|-----|
| 0   | 1   | 2   | 30  |
| 1   | 4   | 5   | 6   |
| 2   | 7   | 8   | 9   |

また以下のようにすると1行目のデータ(配列)にアクセスできます.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(data[0])
```

```
[1, 2, 3]
```

### 練習問題1-1

`data[2][0]`の値を`print()`を使って表示してください

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# この下にプログラムを書く
```

### 練習問題1-2

`data[2][2]`の中身を`90`に書き換えてください.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# この下にプログラムを書く


# ここは変更しないでください
for _ in data:
    print(_)
```

---

## 1.3 二次元配列の表示

二次元配列の中身全体を出力したい時に以下のようにします.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(data)
```

出力結果は以下のようになります.

```
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

このままでは見にくいですが, for文を使うと見やすくなります.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

for i in range(3):
    print(data[i])
```

出力結果は以下のようになります.

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

またこのように書くこともできます.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

for i in range(3):
    for j in range(3):
        print(data[i][j], end='')
    print()
```

出力は以下のようになります.

```
123
456
789
```

二次元配列を操作する例として全ての値を0に書き換えてみます.

```python
# 二次元配列を用意
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# 二次元配列の表示
for i in range(3):
    for j in range(3):
        print(data[i][j], end='')
    print()
print()

# 二次元配列の全ての値を0にする
for i in range(3):
    for j in range(3):
        data[i][j] = 0

# 二次元配列の表示
for i in range(3):
    for j in range(3):
        print(data[i][j], end='')
    print()
```

出力結果は以下のようになります.

```
123
456
789

000
000
000
```

二次元配列の中身を確認する機会は非常に多い為, 以下のような関数を作成します.

```python
def show_data(d):
    for i in d:
        for j in i:
            print("{:^3d}".format(j), end='')
        print()
    print()
```

この関数を使用すると二次元配列の中身を簡単に確認できます.

```python
def show_data(d):
    for i in d:
        for j in i:
            print("{:^3d}".format(j), end='')
        print()
    print()


data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

show_data(data)
```

```
 1  2  3 
 4  5  6 
 7  8  9 
```

> 2重のfor文を用いて配列にアクセスする方法はよく覚えておきましょう.

### 練習問題1-3

以下の二次元配列の各値を2倍したものを表示してください.
先ほど作成した`show_data()`を使用すること推奨します.

```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
```

期待する出力は以下の通りです.

```
 1  2  3 
 4  5  6 
 7  8  9 

 2  4  6 
 8 10 12 
14 16 18 
```

---

## 1.4 二次元配列の初期化

例えば, 0で初期化された3×4の二次元配列を生成したい場合は以下のようにします.

```python
row = 3  # 行
col = 4  # 列
value = 0  # 初期値

data = [[value for j in range(col)] for i in range(row)]
```

|     | 0   | 1   | 2   | 3   |
|-----|-----|-----|-----|-----|
| 0   | 0   | 0   | 0   | 0   |
| 1   | 0   | 0   | 0   | 0   |
| 2   | 0   | 0   | 0   | 0   |

`row`と`col`, `value`の値を書き換えることで, 二次元配列の大きさと初期値を設定できます.
少々ややこしい書き方ですがここでは説明しません.
詳しく知りたい人は"リスト内包表記"で調べてみてください.

### 練習問題1-4

`-1`で初期化された10×10の二次元配列を作成し, 表示してください.
以前作成した`show_data()`の使用を推奨します.

期待する出力は以下の通りです.

```
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 
```

# 2. オセロの作成

## 2.1 盤面の作成

オセロは8×8のマス目の盤面を持つゲームです. よって8×8の二次元配列を用ればゲームの盤面を表現できそうです.

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0   |     |     |     |     |     |     |     |     |
| 1   |     |     |     |     |     |     |     |     |
| 2   |     |     |     |     |     |     |     |     |
| 3   |     |     |     | ○   | ●   |     |     |     |
| 4   |     |     |     | ●   | ○   |     |     |     |
| 5   |     |     |     |     |     |     |     |     |
| 6   |     |     |     |     |     |     |     |     |
| 7   |     |     |     |     |     |     |     |     |

ですが**盤面の外**という概念を取り入れてあげた方が今後プログラミングしやすいため10×10の二次元配列で盤面を表現することにします.
`■`は盤面の外を表しています.

|     | 0   | 1   | 2   | 3   | 4   | 5  | 6   | 7   | 8   | 9   |
|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|-----|
| 0   | ■   | ■   | ■   | ■   | ■   | ■  | ■   | ■   | ■   | ■   |
| 1   | ■   |     |     |     |     |    |     |     |     | ■   |
| 2   | ■   |     |     |     |     |    |     |     |     | ■   |
| 3   | ■   |     |     |     |     |    |     |     |     | ■   |
| 4   | ■   |     |     |     | ○   | ●  |     |     |     | ■   |
| 5   | ■   |     |     |     | ●   | ○  |     |     |     | ■   |
| 6   | ■   |     |     |     |     |    |     |     |     | ■   |
| 7   | ■   |     |     |     |     |    |     |     |     | ■   |
| 8   | ■   |     |     |     |     |    |     |     |     | ■   |
| 9   | ■   | ■   | ■   | ■   | ■   | ■  | ■   | ■   | ■   | ■   |

盤面を二次元配列で表現する際, 各マスの状態を数値で表現します.

* 何も置かれていない : 0
* 黒の石 : 1
* 白の石 : 2
* 盤面の外 : -1

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0   | -1  | -1  | -1  | -1  | -1  | -1  | -1  | -1  | -1  | -1  |
| 1   | -1  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | -1  |
| 2   | -1  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | -1  |
| 3   | -1  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | -1  |
| 4   | -1  | 0   | 0   | 0   | 2   | 1   | 0   | 0   | 0   | -1  |
| 5   | -1  | 0   | 0   | 0   | 1   | 2   | 0   | 0   | 0   | -1  |
| 6   | -1  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | -1  |
| 7   | -1  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | -1  |
| 8   | -1  | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | -1  |
| 9   | -1  | -1  | -1  | -1  | -1  | -1  | -1  | -1  | -1  | -1  |

このような二次元配列を作成できればオセロの盤面は完成です.

### 問題2

`othello.py`という名前のファイルを作成して以下のプログラムを書いてください.

```python
SPACE = 0  # 何も置かれていない
BLACK = 1  # 黒
WHITE = 2  # 白
OUT = -1  # 盤面の外(番兵)
SIZE = 10  # 盤面の大きさ
PLAYER = {BLACK: "黒", WHITE: "白"}


def main():


# ここからプログラムを書く


if __name__ == "__main__":
    main()
```

### 問題2-1

-1で初期化された10×10の二次元配列`board`を作成してください.
(練習問題1-4とほぼ同じです)

### 問題2-2

二次元配列を以下のように出力する関数`show_array()`を作成してください.

* 関数名 : `show_array`
* 引数 : `board`
* 戻り値 : 無し

```
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
 ```

### 問題2-3

`board[1][1]`から`board[8][8]`までを0に書き換えてください.

### 問題2-4

`board[4][4]`と`board[5][5]`に2を, `board[4][5]`と`board[5][4]`に1を代入してください.

### 問題2-5

`init_board()`という関数を作成し, 問題2.3 ~ 2.4までの処理をまとめてください.

* 関数名 : `init_board`
* 引数 : `board`
* 戻り値 : 無し

### 問題2-6

問題2-2で作成した`show_array()`を改良して, 以下のように表示する関数`show_board`を作成してください.

* 関数名 : `show_board`
* 引数 : `board`
* 戻り値 : 無し

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

### 模範解答

ここまでの模範解答プログラムを以下に示します.

```python
SPACE = 0  # 何も置かれていない
BLACK = 1  # 黒
WHITE = 2  # 白
OUT = -1  # 盤面の外(番兵)
SIZE = 10  # 盤面の大きさ
PLAYER = {BLACK: "黒", WHITE: "白"}


# 問題2-2
def show_array(board):
    for i in range(SIZE):
        for j in range(SIZE):
            print("{:3d}".format(board[i][j]), end='')
        print()


# 問題2-3 ~ 問題2-5
def init_board(board):
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            board[i][j] = SPACE

    board[4][4] = WHITE
    board[5][5] = WHITE
    board[4][5] = BLACK
    board[5][4] = BLACK


# 問題2-6
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


def main():
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]  # 問題2-1
    init_board(board)
    show_board(board)


if __name__ == "__main__":
    main()

```

出力は以下のようになります.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

---

## 2.2 指し手の取得と石の配置

指し手を取得する方法を考えます.
石を置きたい座標をキーボードで入力して指し手を取得します.
例えば3行目の4列目(Xの位置)に石を置くときは`3 4`と入力します.

|     | 0   | 1   | 2   | 3   | 4   | 5  | 6   | 7   | 8   | 9   |
|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|-----|
| 0   | ■   | ■   | ■   | ■   | ■   | ■  | ■   | ■   | ■   | ■   |
| 1   | ■   |     |     |     |     |    |     |     |     | ■   |
| 2   | ■   |     |     |     |     |    |     |     |     | ■   |
| 3   | ■   |     |     |     | X   |    |     |     |     | ■   |
| 4   | ■   |     |     |     | ○   | ●  |     |     |     | ■   |
| 5   | ■   |     |     |     | ●   | ○  |     |     |     | ■   |
| 6   | ■   |     |     |     |     |    |     |     |     | ■   |
| 7   | ■   |     |     |     |     |    |     |     |     | ■   |
| 8   | ■   |     |     |     |     |    |     |     |     | ■   |
| 9   | ■   | ■   | ■   | ■   | ■   | ■  | ■   | ■   | ■   | ■   |

スペースで区切られた文字を分割したい時は`split`メソッドを使用します.

```python
text = "Hello World"
text_list = text.split(' ')

print(text_list)
```

上のプログラムでは変数`text`に`"Hello World"`というスペースで区切られた文字列を代入しています.
その後, `split(' ')`によってスペースで区切られたそれぞれの文字列がリストデータとして`text_list`に代入されます.

したがって, 出力は以下のようになります.

```python
['Hello', 'World']
```

`split`メソッドについて理解を深めるためもう一つ例を示します.
`"apple,orange,banana"`のようにカンマで区切られた文字列からそれぞれの果物を取り出すには以下のようにします.

```python
fruit = "apple,orange,banana"
fruit_list = fruit.split(',')

print(fruit_list[0])
print(fruit_list[1])
print(fruit_list[2])
```

このプログラムを実行すると以下のように出力されます.

```
apple
orange
banana
```

必要な知識が揃ったので指し手を取得するプログラムを書いていきます.
以前作成した`init_board()`や`show_board()`も使用します.

```python
def main():
    player = BLACK  # 手番の設定
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)
    show_board(board)

    # 指し手の取得
    move = input("指し手を入力してください : ")
    move = move.split(' ')
    i = int(move[0])
    j = int(move[1])

    board[i][j] = player  # 石を置く
    show_board(board)
```

`3 4`を入力すると出力は以下のようになります.

```
        1  2  3  4  5  6  7  8
    -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1   -1  0  0  0  0  0  0  0  0 -1
2   -1  0  0  0  0  0  0  0  0 -1
3   -1  0  0  0  0  0  0  0  0 -1
4   -1  0  0  0  2  1  0  0  0 -1
5   -1  0  0  0  1  2  0  0  0 -1
6   -1  0  0  0  0  0  0  0  0 -1
7   -1  0  0  0  0  0  0  0  0 -1
8   -1  0  0  0  0  0  0  0  0 -1
    -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

指し手を入力してください : 3 4

        1  2  3  4  5  6  7  8
    -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1   -1  0  0  0  0  0  0  0  0 -1
2   -1  0  0  0  0  0  0  0  0 -1
3   -1  0  0  0  1  0  0  0  0 -1
4   -1  0  0  0  2  1  0  0  0 -1
5   -1  0  0  0  1  2  0  0  0 -1
6   -1  0  0  0  0  0  0  0  0 -1
7   -1  0  0  0  0  0  0  0  0 -1
8   -1  0  0  0  0  0  0  0  0 -1
    -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

先ほどのプログラムを改良して指し手を取得する関数`get_move()`を作成します.

* 引数 : `player`
* 戻り値 : `[i, j]`, iは行, jは列を表す

```python
def get_move(player):
    print(PLAYER[player] + "の番です")
    move = input("指し手を入力してください : ")
    move = move.split(' ')
    i = int(move[0])
    j = int(move[1])

    return [i, j]


def main():
    player = BLACK  # 手番の設定
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)
    show_board(board)

    # 指し手の取得
    i, j = get_move(player)

    board[i][j] = player  # 石を置く
    show_board(board)
```

出力は以下のようになります.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : 3 4

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

ここまでプレイヤーが正しい文法で入力してくれる仮定でプログラムを書いていますが, 誤まった文法で入力してしまう場合もあります.

そこで入力チェックを行います.
チェックする項目は以下の通りです.

* 2つの文字がスペース区切りで入力されているか
    * `split`メソッドによって生成された配列の長さが2であるか確かめればOKです.
    * 配列の長さを取得するには`len()`を使います.
* 2つの文字が数字であるか
    * 文字が数字であるかどうかは`isdecimal`メソッドを使います.
    * 文字が数字であれば`int()`を使って数値に変換します.
* 2つの数値が盤面に収まる値か
    * 二つの値が1~8の数値であれば盤面に収まる値です.

入力した値が以上の条件を満たすまで入力を促すようにプログラムを書けば入力チェックは完成です.
プログラムの模範解答を以下に示します.

```python
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
                i = int(i)  # 数値に変換
                j = int(j)  # 数値に変換
                # 2つの数値が盤面に収まる値か
                if 1 <= i <= 8 and 1 <= j <= 8:
                    return [i, j]
        print("正しい形式で入力して下さい\n")

```

出力は以下のようになります.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : hoge
正しい形式で入力して下さい

黒の番です
指し手を入力してください : 10 2
正しい形式で入力して下さい

黒の番です
指し手を入力してください : 3 4

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

最後に黒→白→黒→...のように手番が交代するように`main()`を書き換えていきます.
ここで相手の石の色を返す関数`opp()`を作成しています.
(例えば黒を関数に渡すと白が返ってきます)

* 関数名 : `opp`
* 引数 : `player`
* 戻り値 : 相手の石の色

```python
def opp(player):
    return 3 - player


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board(board)
        i, j = get_move(player)
        board[i][j] = player
        player = opp(player)
```

> 黒は1, 白は2としているので3 - `player`とすれば以下のような結果となります.
> * 3 - 1(黒) = 2(白)
> * 3 - 2(白) = 1(黒)
>
> このような考え方で`opp()`を作成しています.

出力結果は以下のようになります.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : 3 4

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

白の番です
指し手を入力してください : 3 5

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  2  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : hoge
正しい形式で入力して下さい
```

### 模範解答

ここまでの模範解答プログラムを以下に示します.

```python
SPACE = 0  # 何も置かれていない
BLACK = 1  # 黒
WHITE = 2  # 白
OUT = -1  # 盤面の外(番兵)
SIZE = 10  # 盤面の大きさ
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
                i = int(i)  # 数値に変換
                j = int(j)  # 数値に変換
                # 2つの数値が盤面に収まる値か
                if 1 <= i <= 8 and 1 <= j <= 8:
                    return [i, j]
        print("正しい形式で入力して下さい\n")


def opp(player):
    return 3 - player


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

```

## 2.3 石が置けるか調査する

石を置く前に石が置けるかどうか調査する必要があります.
いきなり8方向を調査するのは難しいので一方向を調査する場合を考えます.

`ケース1`

| 0   | 1   | 2   | 3   | 4  | 5  | 6  | 7  | 8   | 9  |
|-----|-----|-----|-----|----|----|----|----|-----|----|
| ■   | X   | ○   | ●   |    |    |    |    |     | ■  |

上表の`X`に黒の石を置く時, これは正当な置き方と言えるでしょう.それでは次の場合はどうでしょうか.

`ケース2`

| 0   | 1   | 2   | 3   | 4   | 5   | 6  | 7  | 8   | 9  |
|-----|-----|-----|-----|-----|-----|----|----|-----|----|
| ■   | X   | ○   | ○   | ○   | ●   |    |    |     | ■  |

白が続いた後に黒があるのでこれも正当な置き方と言えます.
次の場合はどうでしょうか.

`ケース4`

| 0   | 1   | 2   | 3   | 4  | 5  | 6  | 7  | 8   | 9  |
|-----|-----|-----|-----|----|----|----|----|-----|----|
| ■   | X   | ○   | ○   |    |    |    |    |     | ■  |

`ケース5`

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|
| ■   | X   | ○   | ○   | ○   | ○   | ○   | ○   | ○   | ■  |

`ケース4`や`ケース5`では白が続きますがその隣に黒の石が無く, 挟むことができないので不正な置き方です.
次の場合はどうでしょうか.

`ケース6`

| 0   | 1   | 2   | 3   | 4  | 5  | 6  | 7  | 8   | 9  |
|-----|-----|-----|-----|----|----|----|----|-----|----|
| ■   | X   |     |     |    |    |    |    |     | ■  |

`ケース7`

| 0   | 1   | 2   | 3   | 4  | 5  | 6  | 7  | 8   | 9  |
|-----|-----|-----|-----|----|----|----|----|-----|----|
| ■   | X   | ○   |     |    |    |    |    |     | ■  |

`ケース8`

| 0   | 1   | 2   | 3   | 4  | 5  | 6  | 7  | 8   | 9  |
|-----|-----|-----|-----|----|----|----|----|-----|----|
| ■   |     |     |     |    |    |    |    | X   | ■  |

いずれも隣に白の石がないので不正な置き方になります.
つまり条件をまとめると以下のようになります.


> * 隣が相手の石ならさらに隣を見る, 隣が相手の石でないなら不正な指し手
>* さらに隣が自分の石なら正当な指し手, それ以外なら不正な差し手


以上の条件をプログラムで表現できれば正当な指し手かどうか確認できます.

### 問題2-7

長さ10の配列`board`を1行のみから成るオセロの盤面として考えます.
`board[0]`と`board[9]`の値は盤面の外を表す-1で, その他の要素の値は0(空白), 1(黒石), 2(白石)のいずれかです.
要素番号`j`の位置に`player`(黒 or 白)の石を置くとき, 裏返す石の個数を出力する関数`check()`を作成してください.
調査する方向は`board[j+1]`, `board[j+2]`, `board[j+3]`...というようにプラス方向のみで構いません.

* 関数名 : `check`
* 引数 : `board`, `player`(手番), `j`(石を置く位置)
* 戻り値 : 石を置いたときに裏返す石の数

例えば以下のような配列`board`と変数`player`, `j`を引数とする時は2を戻り値とします.

```python
board = [-1, 0, 2, 2, 1, 0, 0, 0, 0, -1]
player = 1  # 黒の手番
j = 1  # 要素番号1の位置に石を置く

print(check(board, player, j))  # 2が出力される
```

盤面のイメージは以下の通りです. `X`の位置, つまり`board[1]`に黒石を置くと`board[4]`の黒石で挟めます.

| 0   | 1   | 2   | 3   | 4   | 5  | 6  | 7  | 8  | 9  |
|-----|-----|-----|-----|-----|----|----|----|----|----|
| ■   | X   | ○   | ○   | ●   |    |    |    |    | ■  |

プログラムをテストする際は新しく`test.py`というテスト用のファイルを作成してください.

もしくは以下のように関数`test()`と関数`check()`を作成し, `if __name__ == "__main__":`以下を書き換えて下さい.

```python
# othello.pyに追記
def check(board, player, j):


# ここの下にプログラムを書く


# othello.pyに追記
def test():
    player = 1
    board = [-1, 0, 2, 2, 1, 0, 0, 0, 0, -1]
    j = 1

    print(check(board, player, j))

    :
    :

    # main()となっている部分をtest()に書き換える
    if __name__ == "__main__":
        test()
```

### 問題2-8

問題2-7の`check()`をマイナス方向にも調査できるように改良した関数`bi_check()`を作成してください.

* 関数名 : `bi-check`
* 引数 : `board`, `player`(手番), `j`(石を置く位置), `dj`(調査する方向)
* 戻り値 : 石を置いたときに裏返す石の数

### 問題2-9

問題2-8の`bi-check()`を二次元配列でも調査できるように改良した関数`count_turn_over()`を作成してください.

* 関数名 : `count_turn_over()`
* 引数 : `board`, `player`(手番), `i`(石を置く行), `j`(石を置く列), `di`(調査する方向), `dj`(調査する方向)
* 戻り値 : 石を置いたときに裏返す石の数

### 問題2-10

問題2-9で作成した`count_turn_over()`を使用して指し手が正当なものか確認する関数`is_legal_move()`を作成してください.

### 模範解答

```python
SPACE = 0  # 何も置かれていない
BLACK = 1  # 黒
WHITE = 2  # 白
OUT = -1  # 盤面の外(番兵)
SIZE = 10  # 盤面の大きさ
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
                i = int(i)  # 数値に変換
                j = int(j)  # 数値に変換
                # 2つの数値が盤面に収まる値か
                if 1 <= i <= 8 and 1 <= j <= 8:
                    return [i, j]
        print("正しい形式で入力して下さい\n")


def opp(player):
    return 3 - player


# 問題2-7
def check(board, player, j):
    look = 1
    while board[j + look] == opp(player):
        look += 1
    if board[j + look] == player:
        return look - 1
    else:
        return 0


# 問題2-8
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


# 問題2-9
def count_turn_over(board, player, i, j, di, dj):
    view = 1
    while board[i + view * di][j + view * dj] == opp(player):
        view += 1

    if board[i + view * di][j + view * dj] == player:
        return view - 1
    else:
        return 0


# 問題2-10
def is_legal_move(board, player, i, j):
    if board[i][j] is not SPACE:
        return False

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if count_turn_over(board, player, i, j, di, dj):
                return True

    return False


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board(board)
        i, j = get_move(player)
        if is_legal_move(board, player, i, j):
            print("石を置けます")
        else:
            print("石を置けません")
        player = opp(player)


if __name__ == "__main__":
    main()

```

## 2.4 石を裏返す

石を裏返す機能はここまでで作成した関数を活用することで実現可能です.
`is_legal_move()`で正当な差し手か検証した後, `count_turn_over()`で8方向それぞれ裏返す石の数を数えます.
その後, for文を使って盤面を書き換えます.

### 問題2-11

指し手が入力されたら石を置き, 挟める石があるなら石を裏返す関数`set_and_turn_over()`を作成して下さい.
ゲームが正常に進行するように`main()`も適宜書き換えてください.

* 関数名 : `set_and_turn_over()`
* 引数 : `board`, `player`, `i`, `j`
* 戻り値 : なし

期待する出力は以下の通りです.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : 3 4

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  1  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

白の番です
指し手を入力してください : 5 6
石を置けません

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  1  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

白の番です
指し手を入力してください : 5 5
石を置けません

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  1  1  0  0  0 -1
5  -1  0  0  0  1  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

白の番です
指し手を入力してください : 5 3

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  1  1  0  0  0 -1
5  -1  0  0  2  2  2  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
```

> 1. `3 4`に黒の石を置きます. 石をひっくり返した後ターンを白にします.
> 2. `5 6`に白の石を置こうとしますが挟める石が無いので, 再度入力を求めます.
> 3. `5 5`に白の石を置こうとしますが既に石が置いてあるので, 再度入力を求めます
> 4. `5 3`に白の石を置きます. 石をひっくり返した後ターンを黒にします.

### 模範解答

模範解答プログラムを以下に示します.

```python
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


def bi_check(board, player, j, dj):
    look = 1
    while board[j + dj*look] == opp(player):
        look += 1
    if board[j + dj*look] == player:
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
                board[i + c*di][j + c*dj] = player
    board[i][j] = player


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board(board)
        i, j = get_move(player)
        if is_legal_move(board, player, i, j):
            set_and_turn_over(board, player, i, j)
            player = opp(player)
        else:
            print("石を置けません")



if __name__ == "__main__":
    main()

```

## 2.5 ゲームの終了と勝敗

オセロは**白も黒も石が置けない**場合, ゲーム終了となります. 
つまり手番が回ってきた時, 石を置ける場所が一か所でもあるか検証できればパスの判定やゲーム終了の判定が可能となります.
この機能も既に作成した関数を活用することで実現可能です.

### 問題2-12

盤面とプレイヤーを入力すると一か所でも石を置けるなら`True`, 一か所も石を置けないなら`False`を戻り値として返す関数`exit_legal_move()`を作成して下さい.
ゲームが正常に進行するように`main()`も適宜書き換えてください.

* 関数名 : `exit_legal_move()`
* 引数 : `board`, `player`
* 戻り値 : `True` または `False`

期待する出力は以下の通りです.
また, 検証を簡単にするため初期盤面を変更しています.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  1  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : 3 4

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  1  1  0  0  0 -1
5  -1  0  0  0  1  1  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

白石を置ける場所がありません. パスします
黒石を置ける場所がありません. ゲームを終了します
```

### 模範解答

模範解答プログラムを以下に示します.

```python
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
    board[5][5] = BLACK
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


def bi_check(board, player, j, dj):
    look = 1
    while board[j + dj*look] == opp(player):
        look += 1
    if board[j + dj*look] == player:
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
                board[i + c*di][j + c*dj] = player

    board[i][j] = player


def exit_legal_move(board, player):
    for i in range(1, SIZE - 1):
        for j in range(1, SIZE - 1):
            if is_legal_move(board, player, i, j):
                return True

    return False


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board(board)
        # もしプレイヤーが石を置けなければパスする
        if not exit_legal_move(board, player):
            print(PLAYER[player] + "石を置ける場所がありません. パスします")
            player = opp(player)
            # 相手も石が置けなければゲーム終了
            if not exit_legal_move(board, player):
                print(PLAYER[player] + "石を置ける場所がありません. ゲームを終了します")
                break

        i, j = get_move(player)
        if is_legal_move(board, player, i, j):
            set_and_turn_over(board, player, i, j)
            player = opp(player)
        else:
            print("石を置けません")


if __name__ == "__main__":
    main()
```

これで殆どオセロは完成ですがどちらが勝利したか判定する必要があります.
オセロの盤面を1マスずつ確認して白と黒, それぞれが何個あるか数えれば良いです.

### 問題2-13

盤面の白と黒の石をそれぞれカウントして勝者を判定する関数`show_winner()`を作成してください.
* 関数名 : `show_winner()`
* 引数 : `board`
* 戻り値 : なし

期待する出力は以下の通りです.
また, 検証を簡単にするため初期盤面を変更しています.

```
       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  0  0  0  0  0 -1
4  -1  0  0  0  2  1  0  0  0 -1
5  -1  0  0  0  1  1  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

黒の番です
指し手を入力してください : 3 4

       1  2  3  4  5  6  7  8
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
1  -1  0  0  0  0  0  0  0  0 -1
2  -1  0  0  0  0  0  0  0  0 -1
3  -1  0  0  0  1  0  0  0  0 -1
4  -1  0  0  0  1  1  0  0  0 -1
5  -1  0  0  0  1  1  0  0  0 -1
6  -1  0  0  0  0  0  0  0  0 -1
7  -1  0  0  0  0  0  0  0  0 -1
8  -1  0  0  0  0  0  0  0  0 -1
   -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

白石を置ける場所がありません. パスします
黒石を置ける場所がありません. ゲームを終了します
###############
黒 : 5, 白 : 0
黒の勝利
###############

Process finished with exit code 0

```

### 模範解答

模範解答プログラムは以下の通りです.

```python
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
    board[5][5] = BLACK
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
    while board[j + dj*look] == opp(player):
        look += 1
    if board[j + dj*look] == player:
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
                board[i + c*di][j + c*dj] = player

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


def main():
    player = BLACK
    board = [[OUT for _ in range(SIZE)] for _ in range(SIZE)]
    init_board(board)

    while True:
        show_board(board)
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

```

これでオセロの完成です. お疲れさまでした.