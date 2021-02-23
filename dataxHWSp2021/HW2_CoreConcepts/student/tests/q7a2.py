test = {   'name': 'q7a2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               "(clf_rf.named_steps['rf'].__class__ "
                                               'if clf_rf.__class__==Pipeline '
                                               'else clf_rf.__class__)\n'
                                               '<class '
                                               "'sklearn.ensemble._forest.RandomForestClassifier'>\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(cross_val_score(clf_rf,X_train,y_train,cv=kf)) '
                                               '> 0.95\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
