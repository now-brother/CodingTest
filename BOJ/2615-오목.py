if __name__ == "__main__":
    concave = [list(map(int, input().split())) for _ in range(19)]

    ans = 0
    Flag = True

    for i in range(19):
        for j in range(19):
            if concave[i][j] == 1 or concave[i][j] == 2:
                num = concave[i][j]
                if j < 15:                                          #가로 한줄
                    if concave[i][j + 1] == num and concave[i][j + 2] == num and concave[i][j + 3] == num and concave[i][j + 4] == num:
                        if j + 5 < 19:
                            if concave[i][j + 5] == num:
                                ans = 0
                            else:
                                if j > 0:
                                    if concave[i][j - 1] == num:
                                        ans = 0
                                    else:
                                        ans = num
                        else:
                            ans = num       
                if i < 15:                                                                  #세로 한줄
                    if concave[i + 1][j] == num and concave[i + 2][j] == num and concave[i + 3][j] == num and concave[i + 4][j] == num:
                        if i + 5 < 19:
                            if concave[i + 5][j] == num:
                                ans = 0
                            else:
                                if i > 0:
                                    if concave[i - 1][j] == num:
                                        ans = 0
                                    else:
                                        ans = num
                        else:
                            ans = num       
                if i < 15 and j < 15:                                                                                        #대각선 아래로 
                    if concave[i + 1][j + 1] == num and concave[i + 2][j + 2] == num and concave[i + 3][j + 3] == num and concave[i + 4][j + 4] == num:
                        if i + 5 < 19 and j + 5 < 19:
                            if concave[i + 5][j + 5] == num:
                                ans = 0
                            else:
                                if i > 0 and j > 0:
                                    if concave[i - 1][j - 1] == num:
                                        ans = 0
                                    else:
                                        ans = num
                        else:
                            ans = num
                if i > 3 and j < 16:                              #대각선 위로
                    if concave[i - 1][j + 1] == num and concave[i - 2][j + 2] == num and concave[i - 3][j + 3] == num and concave[i - 4][j + 4] == num:
                        if i - 5 >= 0 and j + 5 < 19:
                            if concave[i - 5][j + 5] == num:
                                ans = 0
                            else:
                                if i < 18 and j > 0:
                                    if concave[i + 1][j - 1] == num:
                                        ans = 0
                                    else:
                                        ans = num
                        else:
                            ans = num
            if ans != 0:
                print(ans)
                print(i + 1, j + 1)
                Flag = False
                break
        if Flag == False:
            break
        
    if Flag == True:
        print(0)
