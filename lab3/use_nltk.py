import nltk
import pandas as pd
from nltk.tokenize import RegexpTokenizer

data = pd.read_csv('sources.csv')
tokenizer = RegexpTokenizer(r'\w+')
all_words = nltk.FreqDist(w.lower() for w in tokenizer.tokenize(' '.join(data.question.tolist())))
word_features = list(all_words)[:2000]


def document_features(document):
    document_words = set(tokenizer.tokenize(document))
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

data_tuples = data[['question', 'topic']].itertuples(index=False, name=False)
feature_sets = [(document_features(d), c) for (d, c) in data_tuples]
train_set, test_set = feature_sets[100:], feature_sets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print('Accuracy: ', nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(10)
