def Mcdrive():
    global prize
    global cancell
    global continueorder
    global prizebig
    global bigtasty
    global bigtastyprize
    global prizecheese
    global cheeseburger
    global cheeseburgerprize
    global prizebigmac
    global bigmac
    global bigmacprize
    global prizefrench
    global french
    global frenchprize
    global prizenuggets
    global nuggets
    global nuggetsprize
    global prizecoke
    global coke
    global cokeprize
    global prizeice
    global ice
    global iceprize
    global prizepie
    global pie
    global pieprize
    cheeseburger=0
    bigtasty=0
    bigmac=0
    french=0
    nuggets=0
    coke=0
    ice=0
    pie=0
    prizecheese=0
    prizebig=0
    prizebigmac=0
    prizefrench=0
    prizenuggets=0
    prizecoke=0
    prizeice=0
    prizepie=0
    cheeseburgerprize = 3
    bigtastyprize = 4
    bigmacprize = 5
    frenchprize = 2
    nuggetsprize = 3
    cokeprize = 1.5
    iceprize = 2
    pieprize = 2.5
    print('--------------------------')
    print('Welcome in Mcdrive!')
    print('Do you want to order food?("1-Yes" or "2-No")')
    firstchoice = int(input('Your choice: '))
    if firstchoice == 1:
        print(
            'We have: Cheeseburger(1), Big Tasty(2), Big Mac(3), French Fries(4), Nuggets(5), Coke(6), Ice Cream(7), Pie With Pie WIth Cherries(8). ')
    secondchoice = int(input('Your choice(food): '))
    if firstchoice == 2:
        print('See you later')
    if secondchoice == 1:
        print('How many cheeseburgers do you want?')
        cheeseburger = int(input('Your choice(how many cheeseburgers): '))
        print('You ordered', cheeseburger, 'cheeseburger/cheeseburgers')
        if cheeseburger <= 0:
            print('You can\'t order 0 cheeseburgers')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Yoour choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                cheeseburger = int(input('Your choice(how many cheeseburgers): '))
                print('You ordered', cheeseburger, 'cheeseburger/cheeseburgers')
        if cheeseburger >= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 2:
        print('How many Big Tasty do you want?')
        bigtasty = int(input('Your choice(how many Big Tasty): '))
        print('You ordered', bigtasty, 'Big Tasty')
        if bigtasty <= 0:
            print('You can\'t order 0 Big Tasty')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                bigtasty = int(input('Your choice(how many Big Tasty): '))
                print('You ordered', bigtasty, 'Big Tasty')
        if bigtasty >= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 3:
        print('How many Big Macs do you want?')
        bigmac = int(input('Your choice(how many Big Macs): '))
        print('You ordered', bigmac, 'Big Mac/Big Macs')
        if bigmac <= 0:
            print('You can\'t order 0 Big Macs')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                bigmac = int(input('Your choice(how many Big Macs): '))
                print('You ordered', bigmac, 'Big Tasty')
        if bigmac >= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 4:
        print('How many French Fries do you want?')
        french = int(input('Your choice(how many French Fries): '))
        print('You ordered', french, 'French Fries')
        if french <= 0:
            print('You can\'t order 0 French Fries')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                french = int(input('Your choice(how many French Fries): '))
                print('You ordered', french, 'French Fries')
        if french >= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 5:
        print('How many Nuggets do you want?')
        nuggets = int(input('Your choice(how many Nuggets): '))
        print('You ordered', nuggets, 'Nuggets')
        if nuggets <= 0:
            print('You can\'t order 0 Nuggets')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                nuggets = int(input('Your choice(how many Nuggets): '))
                print('You ordered', nuggets, 'Nuggets')
        if nuggets >= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 6:
        print('How many Coke do you want?')
        coke = int(input('Your choice(how many Coke): '))
        print('You ordered', coke, 'Coke')
        if coke <= 0:
            print('You can\'t order 0 Coke')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                coke = int(input('Your choice(how many Coke): '))
                print('You ordered', coke, 'Coke')
        if coke>= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 7:
        print('How many Ice Cream do you want?')
        ice = int(input('Your choice(how many Ice Cream): '))
        print('You ordered', ice, 'Ice Cream')
        if ice <= 0:
            print('You can\'t order 0 Ice Cream')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                ice = int(input('Your choice(how many Ice Cream): '))
                print('You ordered', ice, 'Coke')
        if ice>= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))
    if secondchoice == 8:
        print('How many Pie WIth Cherries do you want?')
        pie = int(input('Your choice(how many Pie WIth Cherries): '))
        print('You ordered', pie, 'Pie WIth Cherries')
        if pie <= 0:
            print('You can\'t order 0 Pie WIth Cherries')
            print('Do you want to cancell?("1-Yes" or "2-No")')
            cancell = int(input('Your choice(cancell): '))
            if cancell == 1:
                Mcdrive()
            if cancell == 2:
                pie = int(input('Your choice(how many Pie WIth Cherries): '))
                print('You ordered', pie, 'Coke')
        if pie>= 1:
            print('Do you want to continue ordering?("1-Yes" or "2-No")')
            continueorder = int(input('Do you want to continue: '))


while True:
    Mcdrive()
    if continueorder == 1:
        continue
    if continueorder == 2:
        prizecheese += cheeseburgerprize * cheeseburger
        prizebig += bigtasty * bigtastyprize
        prizebigmac += bigmacprize * bigmac
        prizefrench += french * frenchprize
        prizenuggets += nuggetsprize * nuggets
        prizecoke += coke * cokeprize
        prizeice += iceprize * ice
        prizepie += pie * pieprize
        prize = prizecheese + prizebig + prizebigmac + prizefrench + prizenuggets + prizecoke + prizeice + prizepie
        print('Your order costs: ', prize , '$')


