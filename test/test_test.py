import unittest
from sql_runner import SQLRunner

sql_runner = SQLRunner()
cursor = sql_runner.execute_create_file()
# cursor = sql_runner.execute_seed_file()

class TestSQLWindowFunctions(unittest.TestCase):

    file = open("../window_functions.py", "r")
    file.read()
