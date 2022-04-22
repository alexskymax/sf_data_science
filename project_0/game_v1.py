"""         Игра угадай число!         """

import numpy as np

number = np.random.randint(1, 101) # think of a number
count = 0
while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: ")) # Input number
    if predict_number > number:
        print("Число должно быть меньше!")
        print()
    elif predict_number < number:
        print("Число должно быть больше!")
        print()
    else:
        print(f"Вы угадали! Это число {number}, за {count} попыток!")
        print()
        break # End game