test = {   'name': 'q5c',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_5c.csv').shape == (2, 2)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 0 <= pd.read_csv('results/result_5c.csv').iloc[0, 1] <= 100\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 3000 <= pd.read_csv('results/result_5c.csv').iloc[1, 1] <= 4000\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
