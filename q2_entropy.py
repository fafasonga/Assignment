import math as m

'''
the function entropy() accepts an n-gram data structure as an input
that is a dictionary with words of the vocabulary as keys and the probabilities
of these words as values

always test your code
'''

def entropy(one_gram):
    ent = 0.
    for key, val in one_gram.iteritems():
        ent = ent + val * m.log(val, 2)
        print -ent
    return -ent

def test_entropy():
    raise NotImplementedError

if __name__ == "__main__":
    test_entropy()
