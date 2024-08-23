import random

def reservoir_sampling_k(stream, k):
    reservoir = []
    
    for i, item in enumerate(stream, start=1):
        if i <= k:
            reservoir.append(item)
        else:
            j = random.randint(1, i)
            if j <= k:
                reservoir[j - 1] = item
    
    return reservoir