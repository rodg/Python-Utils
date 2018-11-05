
def make_deck():
    deck = []
    suits = 'H','D','C','S'
    faces = 'J','Q','K','A'
    values = 2,3,4,5,6,7,8,9,10
    for suit in suits:
        for value in values:
            deck.append((value,suit))
        for face in faces:
            deck.append((face,suit))

    return deck



