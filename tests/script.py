# test number
test_num = 6

# const
problems_dir = '../problems/'
#test_cases_dir = './cases/'

# import
from list import lists
problem = lists[test_num]

# module setup
import sys, importlib
sys.path.append(problems_dir)
#sys.path.append(test_cases_dir)

print('PROBLEM: ' + problem)
importlib.import_module(problem)
importlib.import_module(problem + '_test')
