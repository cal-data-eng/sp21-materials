test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2b.csv').shape == (100, 7)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(pd.read_csv('results/result_2b.csv').iloc[:50, -1].sum(), 39270.961140000014)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
