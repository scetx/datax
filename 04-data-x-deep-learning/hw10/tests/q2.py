test = {   'name': 'q2',
    'points': 6,
    'suites': [   {   'cases': [   {'code': ">>> model.get_layer(index=0).output_shape[1] \n"
  										'300',
                                       'hidden': False,
                                       'locked': False},
                  {'code': ">>> model.get_layer(index=1).output_shape[1] \n"
                      '200',
                                       'hidden': False,
                                       'locked': False},
                  {'code': ">>> model.get_layer(index=2).output_shape[1] \n"
                      '100',
                                       'hidden': False,
                                       'locked': False},
                  {'code': ">>> model.get_layer(index=3).output_shape[1] \n"
                      '10',
                                       'hidden': False,
                                       'locked': False},
                  {'code': ">>> model.get_layer(index=3).get_config()['activation'] \n"
                      '\'softmax\'',
                                       'hidden': False,
                                       'locked': False},
                  {'code': ">>> model.get_layer(index=1).get_config()['activation'] \n"
                      '\'relu\'',
                                       'hidden': False,
                                       'locked': False},                                                                                   
                         
                                    ],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
