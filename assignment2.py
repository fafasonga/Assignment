import re

from math import log

import q1_create_n_gram as q1
from sklearn.metrics import f1_score


def get_train_test_text_arr(filename, topic):
    with open(filename, 'r') as f:
        data = f.read()
        sections = data.split(topic)
        text_arr = []
        for section in sections:
            section = section.rstrip()
            section = re.sub(r"Page \n\d?", "", section)
            section = section.split("\n\n")[0]
            section = section.lower()
            print(section)
            text_arr.append(section)

        train = text_arr[:70]
        test = text_arr[70:]
        return train, test


edu_train, edu_test = get_train_test_text_arr("edu_train.txt", "Education")
exp_train, exp_test = get_train_test_text_arr("exp_train.txt", "Experience")
sum_train, sum_test = get_train_test_text_arr("sum_train.txt", "Summary")

sum_onegram =  q1.create_n_gram(sum_train, 1)
exp_onegram = q1.create_n_gram(exp_train, 1)
edu_onegram = q1.create_n_gram(edu_train, 1)

ngram_list = [sum_onegram, exp_onegram, edu_onegram]


def bayes(text, ngram):
    _lambda = 0.5
    proba = 1
    words = text.split()
    for word in words:
        p = 0.0000001
        if word in ngram:
            p_w = 0
            p = (1 - _lambda) * ngram.get(word) + _lambda * p_w
        proba = proba * p
    return proba


def mle(text, ngram_list):
    proba_list = []
    for ngram in ngram_list:
        proba_list.append(bayes(text, ngram))
    return proba_list.index(max(proba_list))

test_list = [sum_test, exp_test, edu_test]

y_true = []

for index, val in enumerate(test_list):
    y_true.extend([index] * len(val))

y_predict = []

for test in test_list:
    for t in test:
        y_predict.append(mle(t, ngram_list))

print("f1-score: {}".format(f1_score(y_true, y_predict, average="micro")))