test = {   'name': 'q3ci',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> missing_value_df = pd.read_csv('results/result_3c.csv');\n"
                                               '>>> list(missing_value_df.loc[missing_value_df[\'column_name\'] == \'_id\']["percent_missing"])[0] == 0\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
