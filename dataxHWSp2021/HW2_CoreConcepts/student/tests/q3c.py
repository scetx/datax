test = {   'name': 'q3c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> print '
                                               '(np.round([clf_logit.score(X_train,y_train),clf_logit.score(X_test,y_test)],3))\n'
                                               '[0.987 0.965]\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> print(type(clf_logit))\n'
                                               '<class '
                                               "'sklearn.pipeline.Pipeline'>\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'print(cross_val_score(clf_logit,X_train,y_train,cv=kf).round(3))\n'
                                               '[0.989 0.978 0.967 0.956 1.   '
                                               ']\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
