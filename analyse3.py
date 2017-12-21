# Load the library with the iris dataset
from sklearn.datasets import load_iris

# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score
# Load pandas
import pandas as pd

# Load numpy
import numpy as np

# Set random seed
np.random.seed(0)
'''
https://chrisalbon.com/machine-learning/random_forest_classifier_example_scikit.html
'''
df = pd.read_csv('cut1.csv')

print df.head()

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


df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# View the top 5 rows
df.head()


train, test = df[df['is_train']==True], df[df['is_train']==False]

print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:',len(test))

features = df.columns[[8,11,14,17,20,23,26]]
#features = df.columns[[27,28]]
#print features

#y = pd.factorize(train['class2'])[0] - as i already factorised it this is not needed - it essentially will make 1 as 0 and 0 as 1
#y = train['class2']
y = train['currtop10']
#print y



clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features], y)

clf.predict(test[features])

print clf.predict_proba(test[features])[0:10]

#preds = df.target_names[clf.predict(test[features])]

#print preds[0:5]

#print test['class2'].head()
print test['currtop10'].head()
'''
#print "Train Accuracy :: ", accuracy_score(test['class2'], train[features])
print "Test Accuracy  :: ", accuracy_score(test['class2'], clf.predict(test[features]))
print " Confusion matrix ", confusion_matrix(test['class2'], clf.predict(test[features]))
'''
print "Train Accuracy  :: ", accuracy_score(train['currtop10'], clf.predict(train[features]))
print "Test Accuracy  :: ", accuracy_score(test['currtop10'], clf.predict(test[features]))
print " Confusion matrix ", confusion_matrix(train['currtop10'], clf.predict(train[features]))
print " Confusion matrix ", confusion_matrix(test['currtop10'], clf.predict(test[features]))

print "prec score macro ", precision_score(test['currtop10'], clf.predict(test[features]), average="macro")
print "prec score micro ", precision_score(test['currtop10'], clf.predict(test[features]), average="micro")
print "prec score none ", precision_score(test['currtop10'], clf.predict(test[features]), average=None)

print "recal score macro", recall_score(test['currtop10'], clf.predict(test[features]), average="macro")
print "recal score micro", recall_score(test['currtop10'], clf.predict(test[features]), average="micro")
print "recal score none", recall_score(test['currtop10'], clf.predict(test[features]), average=None)

print list(zip(train[features], clf.feature_importances_))
