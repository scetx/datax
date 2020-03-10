test = {   'name': 'q1e',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> '
                                               "df0.describe().loc['count'].sum() "
                                               '== 40\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "df0.loc['most_common_w_count'].sum() "
                                               '== 3308\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "df0.loc['most_common_w_count'].max() "
                                               '== 865\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> df0.loc['Debate char "
                                               "length'].max() == 87488\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
