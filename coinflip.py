import random
import time

def coin_flip ():
    return random.choice(['skull', 'butt'])

if __name__ == "__main__":
    print ("flipping da coin...")
    time.sleep(3)
    result = coin_flip()
    print(f"The result is: {result}!")