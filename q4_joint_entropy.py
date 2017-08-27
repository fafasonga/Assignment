import math as m

'''
the function joint_entropy() accepts an 2-gram data structures as an input
that is a dictionary with word pairs as keys and the probabilities
of these word pairs as values

always test your code
'''

def joint_entropy(two_gram):
    j_ent = 0.
    for key, val in two_gram.iteritems():
        j_ent = j_ent + val * m.log(val, 2)
        print j_ent
    return j_ent

def test_joint_entropy():
    raise NotImplementedError

if __name__ == "__main__":
    test_joint_entropy()
