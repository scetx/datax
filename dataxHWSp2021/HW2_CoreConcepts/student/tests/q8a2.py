test = {   'name': 'q8a2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               "(clf_ab.named_steps['ab'].__class__ "
                                               'if clf_ab.__class__==Pipeline '
                                               'else clf_ab.__class__)\n'
                                               '<class '
                                               "'sklearn.ensemble._weight_boosting.AdaBoostClassifier'>\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(cross_val_score(clf_ab,X_train,y_train,cv=kf)) '
                                               '> 0.96\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
