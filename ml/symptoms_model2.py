import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from decimal import Decimal
import warnings
from sklearn.exceptions import ConvergenceWarning
df_comb = pd.read_csv("dis_sym_dataset_comb.csv")

warnings.filterwarnings("ignore", category=ConvergenceWarning)
warnings.filterwarnings("ignore")
# creation of features and label for training the models
X = df_comb.iloc[:, 1:]
Y = df_comb.iloc[:, 0:1]
#split dataset
# splitting data for training the classifiers and testing
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.10)
# LR Classifier
lr = LogisticRegression(C=0.0001, max_iter=100, penalty='none', solver='lbfgs')
lr = lr.fit(X, Y)
# prediction of labels for the test data
lr_pred = lr.predict(x_test)
acc_lr = round(Decimal(accuracy_score(y_test, lr_pred) * 100), 2)

print(f"Accuracy (LR) : {acc_lr}%")
# Cross Validation Accuracy LR
# performing cross validation with 5 different splits
scores_lr = cross_val_score(lr, X, Y, cv=5)
# mean of cross val score (accuracy)
score = scores_lr
print(f"Cross Validation Accuracy (LR): {score}%")
with open("symptoms_model.pkl","wb") as fp:
    pickle.dump(lr,fp)

'''param_grid = [
    {'penalty': ['l1', 'l2', 'none'],
     'C': np.logspace(-3, 3, 7)  ,# np.logspace(-4, 4, 20),
     'solver': ['lbfgs', 'newton-cg', 'liblinear'],
     'max_iter': [100, 1000, 2500, 5000]
     }
]


grid = GridSearchCV(LogisticRegression(),
                    param_grid=param_grid, verbose=3, n_jobs=-1)

grid.fit(X, Y)
print(grid.best_estimator_)
print(grid.best_params_)
with open("grid_best.pkl","wb") as fp:
    pickle.dump(grid,fp)'''
'''symp = list(X.columns)
print(list(X.columns))
with open("dataset/symptoms.pkl","wb") as fp:
    pickle.dump(symp,fp)'''
'''with open("dataset\list_diseaseNames.pkl", "rb") as fp:
    print(pickle.load(fp))'''
