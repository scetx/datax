test = {   'name': 'q32b',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> svm_model.__class__\n'
                                               'sklearn.svm._classes.SVC',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(svm_model.predict(x_train_3) '
                                               '== y_train_3) > 0.99\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.mean(svm_model.predict(x_val_3) '
                                               '== y_val_3) > 0.50\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
