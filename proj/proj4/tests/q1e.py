test = {   'name': 'q1e',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> import pickle;\n'
                                               '>>> reviews_boolean_ans_1e = len(pickle.load(open("results/result_1e_1.p", "rb")));\n'
                                               '>>> "reviews_boolean" in pickle.load(open("results/result_1e_2.p", "rb" )) and reviews_boolean_ans_1e == 7500\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
