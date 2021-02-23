test = {   'name': 'q5c2',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               "(clf_svm_poly.named_steps['svc'].kernel "
                                               'if '
                                               'clf_svm_poly.__class__==Pipeline '
                                               'else clf_svm_poly.kernel)\n'
                                               'poly\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(cross_val_score(clf_svm_poly,X_train,y_train,cv=kf)) '
                                               '> 0.975\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
