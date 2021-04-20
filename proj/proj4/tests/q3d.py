test = {   'name': 'q3d',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> important_attribute_business_df = pd.read_csv('results/result_3d.csv');\n"
                                               '>>> len(important_attribute_business_df) == 999 and len(important_attribute_business_df.columns) != 58\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> important_attribute_business_df = pd.read_csv('results/result_3d.csv');\n>>> len(important_attribute_business_df.columns) == 38\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
