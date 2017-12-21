import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.metrics import confusion_matrix
'''
http://dataaspirant.com/2017/02/01/decision-tree-algorithm-python-with-scikit-learn/
'''

df = pd.read_csv('cut1.csv')

print df.shape
df['-1top10'] = df['-1top10'].map({'yes': 1, 'no': 0})
df['-2top10'] = df['-3top10'].map({'yes': 1, 'no': 0})
df['-3top10'] = df['-3top10'].map({'yes': 1, 'no': 0})
df['-4top10'] = df['-4top10'].map({'yes': 1, 'no': 0})
df['-5top10'] = df['-5top10'].map({'yes': 1, 'no': 0})
df['-6top10'] = df['-6top10'].map({'yes': 1, 'no': 0})
df['-7top10'] = df['-7top10'].map({'yes': 1, 'no': 0})

df['currtop10'] = df['currtop10'].map({'yes': 1, 'no': 0})
#df['all7'] = df['all7'].map({'yes': 1, 'no': 0})
#df['class2'] = df['class2'].map({'yes': 1, 'no': 0})

print df
#[9,12,15,18,21,24,27]
'''
X = df.values[:, 8:9]
Y = df.values[:,28]
'''
X = df.values[:, [8,11,14,17,20,23,26]]
Y = df.values[:,27]


X=X.astype('int')
Y=Y.astype('int')
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.33, random_state = 100)

'''
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=10, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=10, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
print "Accuracy is ", accuracy_score(y_test,y_pred)*100
#96.7543138866
'''



'''
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=10, min_samples_leaf=5)#98.4310795667
clf_entropy.fit(X_train, y_train)

clf_entropy = DecisionTreeClassifier(criterion = "entropy", splitter = 'random', max_leaf_nodes = 5, min_samples_leaf = 5, max_depth= 10)#98.4310795667
clf_entropy.fit(X_train,y_train)
'''
clf_entropy = DecisionTreeClassifier(criterion = "entropy", splitter = 'random', max_leaf_nodes = 10, min_samples_leaf = 5, max_depth= 10)#98.4310795667
clf_entropy.fit(X_train,y_train)


y_pred_en = clf_entropy.predict(X_test)
print "pred below?", y_pred_en
strings = ""
for x in y_pred_en:
    strings += str(x) + ","
print strings
#print " Confusion matrix ", confusion_matrix(test['currtop10'], clf.predict(test[features]))

print " Confusion matrix ", confusion_matrix(y_test, y_pred_en)
#print "score?? ", clf_entropy.score(X_test, y_test) - same as precision_score
print "Accuracy is ", accuracy_score(y_test,y_pred_en)*100
#print "Accuracy is train ", accuracy_score(y_train,y_pred_en)*100
#96.7543138866
'''
http://benalexkeen.com/decision-tree-classifier-in-python-using-scikit-learn/
'''
tree.export_graphviz(clf_entropy.tree_, out_file='tree.dot', feature_names=X)

from subprocess import call

call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])
