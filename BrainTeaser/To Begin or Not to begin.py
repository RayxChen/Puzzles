import numpy as np

def monte_carlo(k, n_simulations=100000):
    bag = np.array([0 for _ in range(k)] + [1])
    shuffled_bags = np.array([np.random.permutation(bag) for _ in range(n_simulations)])
    red_idx = np.argmax(shuffled_bags==1, axis=1)
    res = red_idx % 2 == 0
    PA = np.mean(res)
    
    return PA, 1-PA 

if __name__ == '__main__':

    print(monte_carlo(k=6)) # ~ (0.575, 0.425)
    print(monte_carlo(k=5)) # ~ (0.5, 0.5)
