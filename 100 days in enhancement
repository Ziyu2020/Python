from random import randint
money = int(input('define how much money you have: '))
i = 0  # irratation
while money > 0:
    go_on = False
    while True:
        debt = int(input('define the debt for 1 circle： '))
        if 0 < debt < money:
            break
    first = randint(1,6) + randint(1,6)
    i += 1
    print('the %d th points in total is: %d' % (i, first)) 
    if first == 7 or first == 11:
        money += debt
        print('player wins! your money is: %d' % money)
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('player loses! your money is: %d' % money)
    else:
        go_on = True
        second = randint(1,6) + randint(1,6)
        while go_on:
            i += 1
            print('the %d th points in total is: %d' % (i, second))
            if second == 7:
                money -= debt
                print('player loses! your money is: %d' % money)
                go_on = False
            elif second == first:
                money += debt
                print('player wins! your money is: %d' % money)
                go_on = False
            else:
                go_on =True
print('you bankcrupt! game over')
