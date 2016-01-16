import numpy as np
from sklearn.linear_model import LogisticRegression

import csv


class FeatureDetector():
    # set up and cache bad words
    def __init__(self):
        self.badwords = set()

        with open("badlist.txt") as bad_words_file:
            for word in bad_words_file:
                self.badwords.add(word.strip())

        self.features = [self.ratio_bad_words]

    # ratio of bad words to good words
    def ratio_bad_words(self, sentence):
        result = 0

        for word in sentence.lower().split():
            if word in self.badwords:
                result += 1

        return float(result) / (len(sentence) - result)

    # goes through all the features and returns an array of values
    def vector(self, sentence):
        feature_vector = [0 for _ in self.features]

        for i, func in enumerate(self.features):
            feature_vector[i] = func(sentence)

        return np.array(feature_vector)


def read_solutions(filename="test_with_solutions.csv"):
    fd = FeatureDetector()

    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            is_insult = bool(row[0] == "1")
            sentence = row[2]

            sentence_features = fd.vector(sentence)
            print(sentence_features, is_insult)

if __name__ == "__main__":
    read_solutions()

    # do something with this later
    # logreg = LogisticRegression(tol=1e-8, penalty='l2', C=1.5)
