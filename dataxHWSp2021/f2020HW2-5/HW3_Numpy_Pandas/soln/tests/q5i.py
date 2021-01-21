test = {   'name': 'q5i',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q5i' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> (result_q5i[[c for c in '
                                               'result_q5i.columns if '
                                               "c.lower().replace(' "
                                               "','').startswith('gdp/')][0]].fillna(0).astype(float).round(2) "
                                               '== result_q5i[[c for c in '
                                               'result_q5i.columns if '
                                               "c.lower().replace(' "
                                               "','').startswith('gdp/')][0]].fillna(0)).all()\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
