bids = []
names = []

def silentAuction():
    count = 0
    bidders = int(input('Enter the amount of bidders: '))
    while count < bidders:
        count += 1
        name = input('Enter name: ')
        names.append(name)
        bid = int(input('Enter bid: '))
        bids.append(bid)

    winner = max(bids)
    winnerIndex = bids.index(winner)
    print (names[winnerIndex])

silentAuction()