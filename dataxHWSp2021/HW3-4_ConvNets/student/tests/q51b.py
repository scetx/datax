test = {   'name': 'q51b',
    'points': 25,
    'suites': [   {   'cases': [   {   'code': '>>> all([isinstance(layer, '
                                               '(keras.layers.Conv2D, '
                                               'keras.layers.AveragePooling2D, '
                                               '\\\n'
                                               '...                         '
                                               'keras.layers.MaxPooling2D, '
                                               'keras.layers.Flatten, \\\n'
                                               '...                         '
                                               'keras.layers.Dense, '
                                               'keras.layers.BatchNormalization, '
                                               '\\\n'
                                               '...                         '
                                               'keras.layers.Dropout)) for '
                                               'layer in cnn_model.layers])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'cnn_model.evaluate(x_train_5, '
                                               'y_train_5, verbose=0)[1] > '
                                               '0.70\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'cnn_model.evaluate(x_val_5, '
                                               'y_val_5, verbose=0)[1] > 0.69\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
