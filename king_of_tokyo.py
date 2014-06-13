giimport random
def throw_dice():
    result = random.randint(1, 6)
    if result <= 3:
        return result
    elif result == 4:
        return "Heart"
    elif result == 5:
        return "Attack"
    else:
        return "Energy"

def throw_roll(num_dice = 6):
    num_1 = 0
    num_2 = 0
    num_3 = 0
    for i in range(num_dice):
        r = throw_dice()
        if r == 1:
            num_1 += 1
        elif r == 2:
            num_2 += 1
        elif r == 3:
            num_3 += 1
    return [num_1, num_2, num_3]
    V = 0
    if num_1 >= 3:
        V += 1 + (num_1 - 3)
    if num_2 >= 3:
        V += 2 + (num_2 - 3)
    if num_3 >= 3:
        V += 3 + (num_3 - 3)
    return V

def get_expected_value():
    S = float(0)
    for i in range(10000):
        r = throw_roll()
        S += r
        print r
    return S / 10000

expected_value = get_expected_value()
print expected_value