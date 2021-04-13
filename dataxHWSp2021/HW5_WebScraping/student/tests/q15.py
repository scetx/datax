test = {   'name': 'q15',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "df.describe().loc['count'].sum() "
                                               '>= 25\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "df.loc['most_common_w_count'].sum() "
                                               '>= 5000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "df.loc['most_common_w_count'].max() "
                                               '>= 800\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> df.loc['Debate char "
                                               "length'].sum() >= 525000\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> df.loc['Debate char "
                                               "length'].max() >= 95000\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
