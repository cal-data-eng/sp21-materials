test = {   'name': 'q4c',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_4c.csv').shape == (100, 10)\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.isclose(pd.read_csv('results/result_4c.csv').iloc[:50]['interpolated'].sum(), 195.94525) or "
                                               "np.isclose(pd.read_csv('results/result_4c.csv').iloc[:50]['interpolated'].sum(), 369.7514880904479)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
