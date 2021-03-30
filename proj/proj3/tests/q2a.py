test = {   'name': 'q2a',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> pd.read_csv('results/result_2a.csv').shape == (100, 6)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> pd.read_csv('results/result_2a.csv').iloc[:50]['median'].sum() == 34994.4\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(pd.read_csv('results/result_2a.csv').iloc[:50]['mad'].sum(), 802.6000000000022)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
