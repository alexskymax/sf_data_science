"""Game guess number.
The computer itself guesses and guesses the number itself.
"""
import numpy as np


def random_predict(number = 1) -> int:
  """Random guess number

  Args:
    number (int, optional): Random number.

  Returns:
    int: Count of attempts
  """
  count = 0
  min_range = 1
  max_range = 101
  predict = np.random.randint(min_range,max_range) # Generated number to compare
                                                      
  while True: # Starting cycle while
    count += 1 # Starting count
    if number > predict:
      min_range = predict # Change min_range
      predict = np.random.randint(min_range,max_range)
                    
    elif number < predict:
      max_range = predict # Change max_range
      predict = np.random.randint(min_range,max_range)
        
    elif number == predict:
      break # End cycle
        
  return count
    

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

if __name__ == "__main__":
    # RUN
    score_game(random_predict)