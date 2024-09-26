def pascals_triangle(n: int) -> None:
    pt = [[]] * n
    for i in range(n):
        pt[i] = [0]*(i+1)
        pt[i][0] = 1
        for j in range(1,i):
            pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
        pt[i][i] = 1
    for i in pt:
        print(i)
    
pascals_triangle(5)