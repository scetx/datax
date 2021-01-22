test = {   'name': 'q4e',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q4e' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> result_q4e.shape\n(7,)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> ' "
                                               "'.join(np.sort(result_q4e)) == "
                                               "' "
                                               "'.join(np.sort(df['Area'].unique()))\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
