test = {   'name': 'q2b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2b.csv').shape == (100, 7)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(pd.read_csv('results/result_2b.csv').iloc[:50, -1].sum(), 38323.42428000002)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
