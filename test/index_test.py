import unittest, psycopg2, datetime, sys
sys.path.insert(0, '..')
from window_functions import *
from decimal import *


class TestSQLWindowFunctions(unittest.TestCase):
    def test_select_distinct_total_location_sales_on_april_23(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("../seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [('Bowery', 170), ('Bryant Park', 75), ('Tribeca', 45), ('Union Square', 110)]

        cursor.execute(select_distinct_total_location_sales_on_april_23())
        test = cursor.fetchall()

        self.assertEqual(test, result)


    def test_select_distinct_location_and_avg_amount_partitioned_by_location(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("../seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [('Union Square', Decimal('45.7142857142857143')), ('Tribeca', Decimal('67.5000000000000000')), ('Bowery', Decimal('81.6666666666666667')), ('Bryant Park', Decimal('26.8750000000000000'))]

        cursor.execute(select_distinct_location_and_avg_amount_partitioned_by_location())
        test = cursor.fetchall()

        self.assertEqual(test, result)


    def test_select_distinct_date_and_total_company_wide_sales_split_by_date_ordered_by_date(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("../seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [(datetime.date(2018, 4, 21), 350), (datetime.date(2018, 4, 22), 545), (datetime.date(2018, 4, 23), 400)]

        cursor.execute(select_distinct_date_and_total_company_wide_sales_split_by_date_ordered_by_date())
        test = cursor.fetchall()

        self.assertEqual(test, result)


    def test_select_rank_the_sales_of_each_location_from_highest_to_lowest(self):
        connection = psycopg2.connect(database="window_functions_db", host="localhost")
        cursor = connection.cursor()
        seed = open("../seed.sql", "r")
        sql = seed.read()
        cursor.execute(sql)

        result = [('Bowery', 90, 1), ('Bowery', 90, 1), ('Bowery', 80, 3), ('Bowery', 80, 3), ('Bowery', 80, 3), ('Bowery', 70, 6), ('Bryant Park', 40, 1), ('Bryant Park', 30, 2), ('Bryant Park', 30, 2), ('Bryant Park', 30, 2), ('Bryant Park', 25, 5), ('Bryant Park', 20, 6), ('Bryant Park', 20, 6), ('Bryant Park', 20, 6), ('Tribeca', 100, 1), ('Tribeca', 75, 2), ('Tribeca', 50, 3), ('Tribeca', 45, 4), ('Union Square', 80, 1), ('Union Square', 60, 2), ('Union Square', 50, 3), ('Union Square', 40, 4), ('Union Square', 30, 5), ('Union Square', 30, 5), ('Union Square', 30, 5)]

        cursor.execute(select_rank_the_sales_of_each_location_from_highest_to_lowest())
        test = cursor.fetchall()

        self.assertEqual(test, result)
