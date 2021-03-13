test = {   'name': 'q42a',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> all([isinstance(layer, '
                                               '(keras.layers.Dense, '
                                               'keras.layers.BatchNormalization, '
                                               'keras.layers.Dropout)) for '
                                               'layer in fc_model.layers])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'fc_model.evaluate(x_train_4, '
                                               'y_train_4, verbose=0)[1] > '
                                               '0.50\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> fc_model.evaluate(x_val_4, '
                                               'y_val_4, verbose=0)[1] > 0.45\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
