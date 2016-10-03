from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import f_classif
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.svm import SVC



def Logistic_pipeline():
    '''
    This method sets the pipeline for execution to follow.
    '''
    pipeline = Pipeline(steps=[('minmaxer', MinMaxScaler()),
                               ('selection', SelectKBest(score_func=f_classif)),
                               ('reducer', PCA()),
                               ('classifier', LogisticRegression())
                               ])

    return pipeline                        

def Logistic_params(all_parameters=False):
    '''
    To try the GridCVSearch, set all_parameters to true. This has been set to the best parameters already.
    '''
    params = {'reducer__n_components': [.5], 
              'reducer__whiten': [False],
              'classifier__class_weight': ['auto'],
              'classifier__tol': [1e-64], 
              'classifier__C': [1e-3],
              'selection__k': [17]
              }
              
    if all_parameters:
        params = {'selection__k': [7, 9, 12, 17, 'all'],
                  'classifier__C': [1e-07, 1e-05, 1e-2, 1e-1, 1, 10],
                  'classifier__class_weight': [{True: 12, False: 1},
                                               {True: 10, False: 1},
                                               {True: 8, False: 1}],
                  'classifier__tol': [1e-1, 1e-4, 1e-16,
                                      1e-64, 1e-256],
                  'reducer__n_components': [1, 2, 3],
                  'reducer__whiten': [True, False]
                  }
                 
    return params


def LinearSVM_pipeline():
    pipeline = Pipeline(steps=[('minmaxer', MinMaxScaler()),
                               ('selection', SelectKBest(score_func=f_classif)),
                               ('reducer', PCA()),
                               ('classifier', LinearSVC())
                               ])
                               
    return pipeline                        

def LinearSVM_params(all_parameters=False):
    params = {'reducer__n_components': [.5], 
              'reducer__whiten': [True],
              'classifier__class_weight': ['auto'],
              'classifier__tol': [1e-32], 
              'classifier__C': [1e-5],
              'selection__k': [17]
              }
              
    if all_parameters:
        params = {'selection__k': [9, 12, 15, 17, 20],
                  'classifier__C': [1e-15, 1e-5, 1e-2, 1e-1, 1, 10, 100],
                  'classifier__class_weight': [{True: 12, False: 1},
                                               {True: 10, False: 1},
                                               {True: 8, False: 1},
                                               {True: 15, False: 1},
                                               {True: 20, False: 1}],
                  'classifier__tol': [1e-1, 1e-2, 1e-4, 1e-8, 1e-16,
                                      1e-32, 1e-64, 1e-128, 1e-256],
                  'reducer__n_components': [.25, .5, .75, .9, 1, 2, 3, 4, 5],
                  'reducer__whiten': [True, False]
                  }
                 
    return params

    
def RbfSVM_pipeline():
    pipeline = Pipeline(steps=[('minmaxer', MinMaxScaler()),
                               ('selection', SelectKBest(score_func=f_classif)),
                               ('reducer', PCA()),
                               ('classifier', SVC())
                               ])
                               
    return pipeline                        

def RbfSVM_params(all_parameters=False):    
    params = {'reducer__n_components': [.5], 
              'reducer__whiten': [True],
              'selection__k':[17],
              'classifier__C': [1],
              'classifier__gamma': [0.0],
              'classifier__kernel': ['rbf'],
              'classifier__tol': [1e-3],
              'classifier__class_weight': ['auto'],
              'classifier__random_state': [42],
              }
              
    if all_parameters:
        params = {'selection__k': [9, 15, 17, 21],
                  'classifier__C': [1e-5, 1e-2, 1e-1, 1, 10, 100],
                  'classifier__class_weight': [{True: 12, False: 1},
                                               {True: 10, False: 1},
                                               {True: 8, False: 1},
                                               {True: 15, False: 1},
                                               {True: 4, False: 1},
                                               'auto', None],
                  'classifier__tol': [1e-1, 1e-2, 1e-4, 1e-8, 1e-16,
                                      1e-32, 1e-64, 1e-128, 1e-256],
                  'reducer__n_components': [1, 2, 3, 4, 5, .25, .4, .5, .6,
                                            .75, .9, 'mle'],
                  'reducer__whiten': [True, False]
                  }
                 
    return params