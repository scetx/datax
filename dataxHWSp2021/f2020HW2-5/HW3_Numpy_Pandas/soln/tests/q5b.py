test = {   'name': 'q5b',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> dftmp.shape == (56,8) or '
                                               'dftmp.shape == (56,11)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "dftmp.sort_values(['Year','Area "
                                               "Id','Variable "
                                               "Name']).to_csv(index=False) == "
                                               "df3[df3['Area']=='Iceland'].sort_values(['Year','Area "
                                               "Id','Variable "
                                               "Name']).to_csv(index=False)\n"
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
