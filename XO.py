theBoadrd = {'tl': ' ', 'tm': ' ', 'tr': ' ',
             'ml': ' ', 'mm': ' ', 'mr': ' ',
             'bl': ' ', 'bm': ' ', 'br': ' '}


def pri():
    print(theBoadrd['tl'] + '|' + theBoadrd['tm'] + '|' + theBoadrd['tr'])
    print('-+-+-')
    print(theBoadrd['ml'] + '|' + theBoadrd['mm'] + '|' + theBoadrd['mr'])
    print('-+-+-')
    print(theBoadrd['bl'] + '|' + theBoadrd['bm'] + '|' + theBoadrd['br'])


pri()
turn = 'X'
count = 0
while count != 9:
    print('Turn =', turn,'\nChoice :')
    sel = input()
    if theBoadrd[sel] == ' ':
        theBoadrd[sel] = turn
        count += 1
    else:
        print('Retry :')
        continue
    pri()
    if (theBoadrd['tl'] == theBoadrd['tm'] == theBoadrd['tr'] == turn) | (theBoadrd['ml'] == theBoadrd['mm'] == theBoadrd['mr'] == turn) | (theBoadrd['bl'] == theBoadrd['bm'] == theBoadrd['br'] == turn):
        print(turn + ' won')
        break
    if (theBoadrd['tl'] == theBoadrd['ml'] == theBoadrd['bl'] == turn) | (theBoadrd['tm'] == theBoadrd['mm'] == theBoadrd['bm'] == turn) | (theBoadrd['tr'] == theBoadrd['mr'] == theBoadrd['br'] == turn) :
        print(turn + ' won')
        break
    if (theBoadrd['tl'] == theBoadrd['mm'] == theBoadrd['br'] == turn) | (theBoadrd['tr'] == theBoadrd['mm'] == theBoadrd['bl'] == turn):
        print(turn + ' won')
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'



