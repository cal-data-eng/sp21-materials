test = {   'name': 'q5c',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_5c.csv').shape == (2, 2)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 0 <= pd.read_csv('results/result_5c.csv').iloc[0, 1] <= 50\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 500 <= pd.read_csv('results/result_5c.csv').iloc[1, 1] <= 600\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
