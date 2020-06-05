test = {   'name': 'q1e',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "df0.describe().loc['count'].sum() "
                                               '>= 30\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "df0.loc['most_common_w_count'].sum() "
                                               '>= 8000\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "df0.loc['most_common_w_count'].max() "
                                               '>= 1300\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> df0.loc['Debate char "
                                               "length'].max() >= 181000\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
