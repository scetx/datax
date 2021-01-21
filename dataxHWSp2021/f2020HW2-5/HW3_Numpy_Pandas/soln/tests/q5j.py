test = {   'name': 'q5j',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> "nri_max" in globals()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "str(int(df_usa['NRI'].sort_values(ascending=False).head(1)[0])) "
                                               'in str(nri_max)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> "nri_max_year" in '
                                               'globals()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "str(df_usa['NRI'].sort_values(ascending=False).head(1).index[0].year) "
                                               'in str(nri_max_year)\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
