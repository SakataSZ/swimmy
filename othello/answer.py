def main():
    pass


if __name__ == "__main__":
    main()
"""
# 練習問題1-1
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(data[2][0])


# 練習問題1-2
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

data[2][2] = 90

for _ in data:
    print(_)
    
    
# 練習問題1-3
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

for i in range(3):
    for j in range(3):
        data[i][j] *= 2

show_data(data)


# 練習問題1-4
def show_data(d):
    for i in d:
        for j in i:
            print("{:^3d}".format(j), end='')
        print()
    print()


row = 10
col = 10
value = -1

data = [[value for j in range(col)] for i in range(row)]

show_data(data)

"""