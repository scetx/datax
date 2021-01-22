test = {   'name': 'q5d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q5d' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> result_q5d.drop('Year', "
                                               "errors='ignore').to_csv() == "
                                               "df3[df3['Area'] == 'United "
                                               'States of '
                                               "America'].set_index('Year').head().drop('Year', "
                                               "errors='ignore').to_csv()\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> result_q5d.index.name\n'
                                               "'Year'",
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
