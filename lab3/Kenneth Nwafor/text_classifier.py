import pandas as pd
import nltk
from nltk.tokenize import word_tokenize


sources = pd.read_csv("sources.csv")

word_doc = [word for _, row in sources.iterrows() for word in word_tokenize(row.question.decode('utf-8'))]
all_words = nltk.FreqDist(w.lower() for w in word_doc)
word_features = list(all_words)[:200]


def document_features(question, question_type):
    question_words = set(word_tokenize(question.decode('utf-8')))
    features = {'type': question_type}
    for word in word_features:
        features[u'contains({})'.format(word)] = (word in question_words)
    return features

featuresets = [(document_features(row['question'], row.topic), row.topic) for _, row in sources.iterrows()]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print('Accuracy: {}'.format(nltk.classify.accuracy(classifier, test_set)))
classifier.show_most_informative_features(5)
