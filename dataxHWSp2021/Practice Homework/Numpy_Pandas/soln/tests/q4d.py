test = {   'name': 'q4d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q4d' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'result_q4d.to_csv(index=False) '
                                               '== '
                                               'df1.drop_duplicates().tail(5).to_csv(index=False)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> "df2" in globals()\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
