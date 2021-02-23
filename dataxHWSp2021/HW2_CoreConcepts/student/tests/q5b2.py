test = {   'name': 'q5b2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               "(clf_svm_rbf.named_steps['svc'].kernel "
                                               'if '
                                               'clf_svm_rbf.__class__==Pipeline '
                                               'else clf_svm_rbf.kernel)\n'
                                               'rbf\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(cross_val_score(clf_svm_rbf,X_train,y_train,cv=kf)) '
                                               '> 0.975\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
