katz_deli = []

def line(katz_deli):
    if not katz_deli:
        print('The line is currently empty.')
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            number = i + 1
            name = katz_deli[i]
            message += f" {number}. {name}"
        print(message)
line(katz_deli)

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    print(f"Welcome, {new_person}. You are number {len(katz_deli)} in line.")
    # import ipdb; ipdb.set_trace()
    # line(katz_deli)
take_a_number(katz_deli, 'Sam')
take_a_number(katz_deli, 'Bill')
take_a_number(katz_deli, 'Sally')

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")
now_serving(katz_deli)