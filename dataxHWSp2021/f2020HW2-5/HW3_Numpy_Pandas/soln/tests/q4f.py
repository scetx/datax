test = {   'name': 'q4f',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> 'result_q4f' in globals()\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "pd.to_datetime(df1.drop_duplicates()['Year'], "
                                               "format='%Y').sort_values().head(4).to_csv(index=False, "
                                               "date_format='%Y%m%d') == "
                                               "result_q4f['Year'].to_csv(index=False, "
                                               "date_format='%Y%m%d')\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': ">>> 'df3' in globals()\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> df3.shape\n(365, 8)',
                                       'hidden': True,
                                       'locked': False},
                                   {   'code': '>>> df3 is df2\nFalse',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
