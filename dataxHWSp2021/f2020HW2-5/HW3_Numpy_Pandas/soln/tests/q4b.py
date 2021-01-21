test = {   'name': 'q4b',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q4b' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'result_q4b.to_csv(index=False) '
                                               '== '
                                               'df.loc[:,~df.isnull().all()][~df.loc[:,~df.isnull().all()].isnull().any(axis=1)].tail(5).to_csv(index=False)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> "df1" in globals()\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> df1.shape\n(420, 8)',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
