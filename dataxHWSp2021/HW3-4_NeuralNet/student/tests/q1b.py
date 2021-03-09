test = {   'name': 'q1b',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'keras.backend.eval(history_1b.model.optimizer.learning_rate) '
                                               '== 1.0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'keras.backend.eval(history_1b.model.optimizer.momentum) '
                                               '> 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "history_1b.history['loss'][4] "
                                               '< 0.08\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
