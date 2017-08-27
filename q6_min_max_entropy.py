import math as m

'''
the function compute_min_max_entropy() accepts an n-gram data structure as an
input that is a dictionary with words of the vocabulary as keys and
the probabilities of these words as values

always test your code
'''

def compute_min_max_entropy(one_gram):
    min_entropy = 0
    max_entropy = 0
    for key, val in one_gram:
        y, x = key.split()
        min_entropy = -(min_entropy + val * m.log(val, 2))
        max_entropy = 1 / (max_entropy + val * m.log(val, 2))

    return min_entropy, max_entropy

def test_compute_min_max_entropy():
    raise NotImplementedError

if __name__ == "__main__":
    test_compute_min_max_entropy()
