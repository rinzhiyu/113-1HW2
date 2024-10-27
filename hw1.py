from typing import List

def getResult():
    # 鍵盤下排
    alphabet1: List[List[chr]] = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], 
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
        ['Z', 'x', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
    ]
    # 鍵盤上排
    alphabet2: List[List[chr]] = [ 
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'x', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
    ]

    n = int(input("請輸入測試筆數: "))
    repeat = set()  # 用來追蹤已經印出的符號，避免重複

    for i in range(n):
        value, direction = input("請輸入符號和方向(用空格隔開)(1:上，2:下，3:右，4:左): ").split()
        direction = int(direction)

        # 在 alphabet1 中尋找
        for j in range(len(alphabet1)):
            if value in alphabet1[j]:
                k = alphabet1[j].index(value)

                if direction == 1:
                    newValue = alphabet1[j - 1][k]
                elif direction == 2:
                    newValue = alphabet1[j + 1][k]
                elif direction == 3:
                    newValue = alphabet1[j][k + 1]
                elif direction == 4:
                    newValue = alphabet1[j][k - 1]
                else:
                    newValue = value

                if newValue not in repeat:
                    print(newValue)
                    repeat.add(newValue)

        # 如果沒在 alphabet1 中找到，則在 alphabet2 中尋找
            for j in range(len(alphabet2)):
                if value in alphabet2[j]:
                    k = alphabet2[j].index(value)

                    if direction == 1:
                        newValue = alphabet2[j - 1][k]
                    elif direction == 2:
                        newValue = alphabet2[j + 1][k]
                    elif direction == 3:
                        newValue = alphabet2[j][k + 1]
                    elif direction == 4:
                        newValue = alphabet2[j][k - 1]
                    else:
                        newValue = value

                    if newValue not in repeat:
                        print(newValue)
                        repeat.add(newValue)

getResult()
