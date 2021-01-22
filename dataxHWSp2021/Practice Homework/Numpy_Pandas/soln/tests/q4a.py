test = {   'name': 'q4a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q4a' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'result_q4a.to_csv(index=False) '
                                               '== '
                                               "df[df['Symbol'].isnull()].head(5).to_csv(index=False)\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
