test = {   'name': 'q4b2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               "(clf_knn.named_steps['knn'].__class__ "
                                               'if clf_knn.__class__==Pipeline '
                                               'else clf_knn.__class__)\n'
                                               '<class '
                                               "'sklearn.neighbors._classification.KNeighborsClassifier'>\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(cross_val_score(clf_knn,X_train,y_train,cv=kf)) '
                                               '> 0.96\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
