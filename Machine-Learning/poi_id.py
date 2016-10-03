#!/usr/bin/python

import sys
import pickle
import evaluate
import feature_add
sys.path.append("../tools/")
from copy import copy
from feature_format import featureFormat, targetFeatureSplit
from sklearn.feature_selection import SelectKBest
from sklearn.decomposition import PCA
from sklearn.feature_selection import f_classif
from sklearn.preprocessing import MinMaxScaler
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.grid_search import GridSearchCV

class_label = ['poi']
financial_features = ['salary', 'deferral_payments', 'total_payments', 'loan_advances', 'bonus', 'restricted_stock_deferred', 'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options', 'other', 'long_term_incentive', 'restricted_stock', 'director_fees']
email_features = ['to_messages', 'from_poi_to_this_person', 'from_messages', 'from_this_person_to_poi', 'shared_receipt_with_poi'] 
my_feature_list = class_label + financial_features + email_features 


### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop("TOTAL", 0)
data_dict.pop('THE TRAVEL AGENCY IN THE PARK', 0)
data_dict.pop('LOCKHART EUGENE E',0)

### Store to my_dataset for easy export below.
my_dataset = copy(data_dict)
### Adding new features to the dataset. Although, these features did not help me meet the 0.3 criterion for precision, therefore I did not use it in the final dataset.
#feature_add.ratiosPOI(my_dataset, my_feature_list)
#feature_add.totalFinance(my_dataset, my_feature_list)

#Preprocessing data and getting it in desired format
data = featureFormat(my_dataset, my_feature_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#StratifiedShuffleSplits for 1000 internal cross-validation splits within the grid-search.
sk_fold = StratifiedShuffleSplit(labels, n_iter=1000, test_size=0.1)

#Calling the Logistic Regression pipeline with best parameters.
pipeline = evaluate.Logistic_pipeline()
params = evaluate.Logistic_params()

#Uncomment below lines to run SVM with Linear and RBF kernel.
#pipeline = evaluate.LinearSVM_pipeline()
#params evaluate.LinearSVM_params()

#pipeline = evaluate.RbfSVM_pipeline()
#params evaluate.RbfSVM_params()


clf_best_fit = GridSearchCV(pipeline, param_grid=params, cv=sk_fold,n_jobs=-1, scoring='recall')
clf_best_fit.fit(features, labels)
mask = clf_best_fit.best_estimator_.named_steps['selection'].get_support()
top_features = [x for (x, boolean) in zip(features, mask) if boolean]
n_pca_components = clf_best_fit.best_estimator_.named_steps['reducer'].n_components_
    
print "Cross-validated {0} score: {1}".format('recall', clf_best_fit.best_score_)
print "{0} features selected".format(len(top_features))
print "Reduced to {0} PCA components".format(n_pca_components)
    
clf = clf_best_fit.best_estimator_


### Task 6: Dump your classifier, dataset, and my_feature_list so anyone can check your results.

pickle.dump(clf, open("my_classifier.pkl", "w"))
pickle.dump(my_dataset, open("my_dataset.pkl", "w"))
pickle.dump(my_feature_list, open("my_feature_list.pkl", "w"))