def card():
    pattern = ['S', 'C', 'H', 'D']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    point = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11'] * 4

    card_form = list()
    card_set = dict()
    for i, j in enumerate(pattern):
        for v, w in enumerate(numbers):
            card_form.append(j + w)
    
    for x in range(52):
        card_set[card_form[x]] = point[x]
    return card_set

print(card())