test = {   'name': 'q6b2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               "(clf_dt.named_steps['dt'].__class__ "
                                               'if clf_dt.__class__==Pipeline '
                                               'else clf_dt.__class__)\n'
                                               '<class '
                                               "'sklearn.tree._classes.DecisionTreeClassifier'>\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(cross_val_score(clf_dt,X_train,y_train,cv=kf)) '
                                               '> 0.92\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
