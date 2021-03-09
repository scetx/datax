test = {   'name': 'q1c',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               'history_1c.model.optimizer.__class__.__name__ '
                                               "!= 'SGD'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "history_1c.history['loss'][4] "
                                               '< 0.07\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'history_1c.model.layers[1].units\n'
                                               '100',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'len(history_1c.model.layers)\n'
                                               '3',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
