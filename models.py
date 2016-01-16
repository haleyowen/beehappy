import csv

import enchant

import numpy as np

from sklearn.linear_model import LogisticRegression

from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import TweetTokenizer


class FeatureDetector():
    # set up and cache bad words
    def __init__(self):
        self.badwords = set()

        # populate bad words from text fil
        with open("badlist.txt") as bad_words_file:
            for word in bad_words_file:
                self.badwords.add(word.strip())

        # used to normalize words "saying" => "say"
        self.stemmer = LancasterStemmer()

        # spellchecker
        self.checker = enchant.Dict("en_US")

        # used to split sentences better
        self.tokenizer = TweetTokenizer(preserve_case=False)

        # list of function pointers of all features
        self.features = [self.ratio_bad_words,
                         self.ratio_cap_characters,
                         self.ratio_mispelled]

    # ratio of bad words to good words
    def ratio_bad_words(self, sentence):
        result = 0

        for word in sentence.lower().split():
            # cut off extra suffix on word
            stemmed = self.stemmer.stem(word)

            if word in self.badwords or stemmed in self.badwords:
                result += 1

        return float(result) / (len(sentence) - result)

    def ratio_cap_characters(self, sentence):
        caps = 0
        total = 0

        for word in sentence.split():
            caps += sum(char.isupper() for char in word)
            total += len(word)

        return float(caps) / (total - caps)

    def ratio_mispelled(self, sentence):
        wrong = 0
        total = 0

        for word in sentence.split():
            if not self.checker.check(word):
                print(word)
                wrong += 1
            total += 1

        return float(wrong) / (total - wrong)

    # goes through all the features and returns an array of values
    def vector(self, sentence):
        feature_vector = [0 for _ in self.features]

        for i, feature in enumerate(self.features):
            feature_vector[i] = feature(sentence)

        return feature_vector


def read_solutions(filename="test_with_solutions.csv"):
    fd = FeatureDetector()
    data = list()

    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            is_insult = bool(row[0] == "1")
            sentence = row[2]

            sentence_features = fd.vector(sentence)

            data.append((is_insult, sentence, sentence_features))

            # find each feature value for this sentence
            # print(sentence_features, is_insult)

    train_X = [tup[2] for tup in data[:2000]]
    train_Y = [tup[0] for tup in data[:2000]]

    test_data = [tup[2] for tup in data[2000:]]
    test_answer = [tup[0] for tup in data[2000:]]

    logreg = LogisticRegression(tol=1e-8, penalty='l2', C=1.5)

    logreg.fit(train_X, train_Y)

    correct = 0
    total = 0

    for X, Y in zip(test_data, test_answer):
        result = logreg.predict(X)
        total += 1
        correct += result == Y

    print(float(correct) / total)
    print(train_X[0])


if __name__ == "__main__":
    read_solutions()

    # do something with this later
