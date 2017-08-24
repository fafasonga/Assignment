import math as m

'''
the function compute_min_max_entropy() accepts an n-gram data structure as an
input that is a dictionary with words of the vocabulary as keys and
the probabilities of these words as values

always test your code
'''

def compute_min_max_entropy(one_gram):
    for key, val in one_gram.iteritems():
        min_entropy = min_entropy + val * m.log(val, 2)
        min_entropy = -min_entropy
        print min_entropy
        print int(m.ceil(min_entropy))

    return min_entropy,max_entropy

def test_compute_min_max_entropy():
    raise NotImplementedError

if __name__ == "__main__":
    test_compute_min_max_entropy()
