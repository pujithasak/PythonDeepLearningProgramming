from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vt = TfidfVectorizer()
tfidf_Vt1 = TfidfVectorizer(ngram_range=(1, 2))
tfidf_Vt2 = TfidfVectorizer(stop_words='english')

X_train = tfidf_Vt.fit_transform(twenty_train.data)
X_train1 = tfidf_Vt1.fit_transform(twenty_train.data)
X_train2 = tfidf_Vt2.fit_transform(twenty_train.data)

clf = MultinomialNB()
clf.fit(X_train, twenty_train.target)

clf0 = SVC()
clf0.fit(X_train, twenty_train.target)

clf1 = MultinomialNB()
clf1.fit(X_train1, twenty_train.target)

clf2 = MultinomialNB()
clf2.fit(X_train2, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)

X_test_tfidf = tfidf_Vt.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = round(metrics.accuracy_score(twenty_test.target, predicted), 4)
print("MultinomialNB accuracy is: ", score)

X_test_tfidf0 = tfidf_Vt.transform(twenty_test.data)
predicted0 = clf0.predict(X_test_tfidf0)
score = round(metrics.accuracy_score(twenty_test.target, predicted0), 4)
print("SVC accuracy is: ", score)


X_test_tfidf1 = tfidf_Vt1.transform(twenty_test.data)
predicted1 = clf1.predict(X_test_tfidf1)
score1 = round(metrics.accuracy_score(twenty_test.target, predicted1), 4)
print("Bigram score: ", score1)


X_test_tfidf2 = tfidf_Vt2.transform(twenty_test.data)
predicted2 = clf2.predict(X_test_tfidf2)
score2 = round(metrics.accuracy_score(twenty_test.target, predicted2), 4)
print("Adding the stop-words score: ", score2)
