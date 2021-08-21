x = int(input())
y = int(input())
g = int(input())

check = True
my2d = []
myFullRow = []
myEmptyRow = []
myUpRow = []
myList = []
upper_space = 0
score = 0
time = 0

if y % 2 == 1:
    left_space = y // 2
    right_space = y // 2
else:
    left_space = int(y/2 - 1)
    right_space = int(y/2)
for k in range(y):
    myUpRow.append(' ')
    for l in range(upper_space):
        if len(myUpRow) == y:
            my2d += [myUpRow[:]]
for k in range(y):
    myFullRow.append('*')
    for i in range(x):
        if len(myFullRow) == y:
            my2d += [myFullRow[:]]
for k in range(y):
    myEmptyRow.append(' ')
    for j in range(g):
        if len(myEmptyRow) == y:
            my2d += [myEmptyRow[:]]
if x == 0:
    print('YOU WON!')
for lst in my2d:
    for elem in lst:
        print(elem, end='')
    print()
print(' '*left_space + '@' + ' '*right_space)
print('-'*72)
if x != 0:
    print('Choose your action!')
else:
    print('YOUR SCORE: ' + str(score))
    check = False

while check:
    command = input()
    time += 1

    if command.lower() == 'exit':
        for lst in my2d:
            for elem in lst:
                print(elem, end='')
            print()
        print(' ' * left_space + '@' + ' '*right_space)
        print('-' * 72)
        print('YOUR SCORE: ' + str(score))
        check = False
        break

    elif command.lower() == 'left':
        if left_space == 0:
            pass
        else:
            left_space -= 1
            right_space += 1

    elif command.lower() == 'right':
        if right_space == 0:
            pass
        else:
            right_space -= 1
            left_space += 1

    elif command.lower() == 'fire':
        gun_space = len(my2d)
        while gun_space > 0:
            gun_space -= 1
            if my2d[gun_space][left_space] == ' ':
                my2d[gun_space][left_space] = '|'
                for lst in my2d:
                    for elem in lst:
                        print(elem, end='')
                    print()
                print(' ' * left_space + '@' + ' ' * right_space)
                print('-' * 72)
                my2d[gun_space][left_space] = ' '
            elif my2d[gun_space][left_space] == '*':
                my2d[gun_space][left_space] = ' '
                score += 1
                break

    else:
        pass

    if time % 5 == 0:
        for k in range(y):
            myList.append(' ')
        my2d.insert(0, list(myList[:]))
        myList.clear()
        if '*' in my2d[-1]:
            print('GAME OVER')
            if time % 5 == 0:
                my2d.pop(0)
            for lst in my2d:
                for elem in lst:
                    print(elem, end='')
                print()
            print(' ' * left_space + '@' + ' ' * right_space)
            print('-' * 72)
            print('YOUR SCORE: ' + str(score))
            check = False
            break
        else:
            my2d.pop(-1)

    count = 0
    for a in my2d:
        for k in a:
            if k =='*':
                count += 1
            else:
                pass
    if count == 0:
        print('YOU WON!')
    for lst in my2d:
        for elem in lst:
            print(elem, end='')
        print()
    print(' ' * left_space + '@' + ' ' * right_space)
    print('-' * 72)
    if count == 0:
        print('YOUR SCORE: ' + str(score))
        check = False
        break
    else:
        print('Choose your action!')