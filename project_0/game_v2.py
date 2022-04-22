"""         Игра угадай число!
Компьютер сам загадывает и угадывает число."""
    
import numpy as np

def random_predict(number:int=1) -> int:
    """Random guess number
    Args:
        number (int, optional): Guess number. Defaults to 1.
    Returns:
        int: Try number
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)     
        if number == predict_number:
            break #End of cycle
    return(count)# Number of attempts
    
    



def score_game(random_predict):
    """How many attempts on average out of 1000 approaches our algorithm guesses

    Args:
        random_predict (_type_): guess func
        
    Returns:
        int: average attempts
    """
    
    count_ls = [] # List for save number attempts 
    np.random.seed(1) # Start number for algoritm generation random numbers
    random_array = np.random.randint(1,101,size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # Average number attempts
    
    print(f"Yours algoritm guess numbers average: {score} attempts!")
    return(score)


if __name__ == '__main__':
    score_game(random_predict)