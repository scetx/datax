test = {   'name': 'q42a',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> np.round(x_train_4, 3)\n'
                                               'array([[0.231, 0.243, 0.247, '
                                               '..., 0.482, 0.361, 0.282],\n'
                                               '       [0.604, 0.694, 0.733, '
                                               '..., 0.561, 0.522, 0.565],\n'
                                               '       [1.   , 1.   , 1.   , '
                                               '..., 0.314, 0.337, 0.329],\n'
                                               '       ...,\n'
                                               '       [0.239, 0.286, 0.298, '
                                               '..., 0.722, 0.627, 0.459],\n'
                                               '       [0.039, 0.016, 0.055, '
                                               '..., 0.686, 0.682, 0.804],\n'
                                               '       [0.686, 0.757, 0.898, '
                                               '..., 0.357, 0.306, 0.353]], '
                                               'dtype=float32)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> y_train_4\n'
                                               'array([[0., 0., 0., ..., 0., '
                                               '0., 0.],\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 1.],\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 1.],\n'
                                               '       ...,\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 0.],\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 1.],\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 0.]], dtype=float32)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> y_val_4\n'
                                               'array([[0., 0., 0., ..., 0., '
                                               '1., 0.],\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 1.],\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 0.],\n'
                                               '       ...,\n'
                                               '       [0., 0., 0., ..., 0., '
                                               '0., 1.],\n'
                                               '       [0., 1., 0., ..., 0., '
                                               '0., 0.],\n'
                                               '       [0., 1., 0., ..., 0., '
                                               '0., 0.]], dtype=float32)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all([isinstance(layer, '
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
