test = {   'name': 'q1a2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'history_1a2.model.optimizer.__class__.__name__\n'
                                               "'SGD'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "history_1a2.history['loss'][4] "
                                               '< '
                                               "history_1a1.history['loss'][4]\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "history_1a2.model.optimizer.learning_rate.__module__.split('.')[-1]\n"
                                               "'learning_rate_schedule'",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
