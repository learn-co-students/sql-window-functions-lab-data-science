import psycopg2, sys

class SQLRunner:
    def __init__(self):
        self.connection = psycopg2.connect(database="lab_db", host="localhost")
        self.cursor = self.connection.cursor()

    def execute_create_file(self):
        import pdb; pdb.set_trace()
        file = open("../create.sql", "r")
        sql = file.read()
        table = self.cursor.execute(sql)
        return table

    def execute_seed_file(self):
        # sql = "INSERT INTO countries(name) VALUES(%s) RETURNING country_id;"
        # file = open("../seed.py", "r")
        # countries = 'countries'
        # self.cursor.execute(sql.SQL("insert into {} values (%s, %s)").format(sql.Identifier('countries')), [(1, "USA",), (2, "Canada",)])

        # sql = file.read()
        # table = self.cursor.execute(sql)
        return table
