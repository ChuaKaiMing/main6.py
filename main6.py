nColumn = int(input('How many columns to display: '))
nRow = int(input('How many rows to display: '))
if nColumn == 0 and nRow == 0:
    exit
elif nColumn == 0 or nRow == 0 or nColumn > 15 or nRow > 15:
    exit
else:
    for a in range(nRow):
        for b in range(3):
            if b % 2 == 0:
                TempoVar = '-----'*nRow
                print(TempoVar)
            else:
                for c in range(nColumn):
                    for d in range(5):
                        if d % 4 == 0:
                            print('|',end='')
                        elif c == len(TempoVar):
                            print('|')
                        else:
                            print(' ',end='')




#    ----- 0                                            -------- row      |
#    |   | 1  1 column                                                    | column
#    ----- 2                                                              |
#    |   | 3
#    ----- 4
#    1 row
