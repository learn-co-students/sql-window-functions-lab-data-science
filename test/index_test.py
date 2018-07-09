import unittest, psycopg2, datetime, sys
sys.path.insert(0, '..')
from window_functions import *
from decimal import *


class TestSQLWindowFunctions(unittest.TestCase):
    def test_select_distinct_total_location_sales_on_april_23(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("./seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [('Brooklyn', 170), ('Houston', 60), ('London', 45), ('New York', 110), ('Washington', 20)]

        cursor.execute(select_distinct_total_location_sales_on_april_23())
        test = cursor.fetchall()

        self.assertEqual(test, result)


    def test_select_distinct_location_and_avg_amount_partitioned_by_location(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("./seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [('New York', Decimal('45.7142857142857143')), ('London', Decimal('67.5000000000000000')), ('Brooklyn', Decimal('81.6666666666666667')), ('Houston', Decimal('28.7500000000000000')), ('Washington', Decimal('26.6666666666666667'))]

        cursor.execute(select_distinct_location_and_avg_amount_partitioned_by_location())
        test = cursor.fetchall()

        self.assertEqual(test, result)


    def test_select_distinct_date_and_total_company_wide_sales_split_by_date_ordered_by_date(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("./seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [(datetime.date(2018, 4, 21), 375), (datetime.date(2018, 4, 22), 575), (datetime.date(2018, 4, 23), 405)]

        cursor.execute(select_distinct_date_and_total_company_wide_sales_split_by_date_ordered_by_date())
        test = cursor.fetchall()

        self.assertEqual(test, result)


    def test_select_rank_the_sales_of_each_location_from_highest_to_lowest(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("./seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [('Brooklyn', 90, 1), ('Brooklyn', 90, 1), ('Brooklyn', 80, 3), ('Brooklyn', 80, 3), ('Brooklyn', 80, 3), ('Brooklyn', 70, 6), ('Houston', 35, 1), ('Houston', 30, 2), ('Houston', 25, 3), ('Houston', 25, 3), ('London', 100, 1), ('London', 75, 2), ('London', 50, 3), ('London', 45, 4), ('New York', 80, 1), ('New York', 60, 2), ('New York', 50, 3), ('New York', 40, 4), ('New York', 30, 5), ('New York', 30, 5), ('New York', 30, 5), ('Washington', 40, 1), ('Washington', 30, 2), ('Washington', 30, 2), ('Washington', 20, 4), ('Washington', 20, 4), ('Washington', 20, 4)]

        cursor.execute(select_rank_the_sales_of_each_location_from_highest_to_lowest())
        test = cursor.fetchall()

        self.assertEqual(test, result)
