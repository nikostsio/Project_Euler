def main():

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    TARGET=200
    matrix = {}
    for y in range(0, TARGET+1):
        matrix[y, 0] = 1 
    for y in range(0, TARGET+1):
        print(y,' '*(3-len(str(y))), ":", 1, end = ' ')
        for x in range(1, len(coins)):
            matrix[y, x] = 0
            if y>=coins[x]:
                matrix[y, x] += matrix[y, x-1]
                matrix[y, x] += matrix[y-coins[x], x]
            else:
                matrix[y, x] = matrix[y, x-1]
            print(matrix[y, x], end = ' '*(8-len(str(matrix[y,x]))))
        print()
if __name__=='__main__':
    main()