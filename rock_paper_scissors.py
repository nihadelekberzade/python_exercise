def calc_winner(a, b):
    if a == 'r' and b == 's' or a == 'p' and b == 'r' or a == 's' and b == 'p':
        print('First player won')
    elif a == 'r' and b == 'p' or a == 'p' and b == 's' or a == 's' and b == 'r':
        print('Second player won')
    else:
        print("Draw")


print("Pick Rock (r), Paper (p) , or Scissors (s)")

player_1 = input('PLayer 1 : ').lower()
player_2 = input('PLayer 2 : ').lower()

calc_winner(player_1, player_2)
