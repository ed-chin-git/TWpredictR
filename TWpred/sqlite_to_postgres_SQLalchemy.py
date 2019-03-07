#  ________
import pandas as pd
import sqlite3
import psycopg2
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite


def verify_output(pgres_engine, table_name):
    # ______  verify output-table contents ____
    query = 'SELECT * FROM ' + table_name + ' LIMIT 10;'
    for row in pgres_engine.execute(query).fetchall():
        print(row)
    return


def run_conversion(pgres_engine):
    # ___ process tables ____
    # - WARNING!  schema must already exist
    schema_name = 'lambdaRPG'
    tables = ['user',
              'tweet']

    # ___ connect to  sqlite3  ____
    lite_engine = create_engine('sqlite+pysqlite:///twpred.db',
                                module=sqlite)

    for table_name in tables:
        print('converting........ ', table_name)
        # ___ load SQlite into df   ____
        df = pd.read_sql_table(table_name,
                               con=lite_engine)

        #  BUG ALERT! drop the dataframe index column
        #             before executing .to_sql()

        # ___ Convert to postgres DB____
        df.to_sql(table_name,
                  if_exists='replace',
                  con=pgres_engine,
                  schema=schema_name,
                  method='multi')
        verify_output(pgres_engine, table_name)

    return


def main():
    # __ Connect to postgres (SQLalchemy.engine) ____
    pgres_str = 'postgres://nylykskjdubnhn:eae3b8a9de3683a7513126b5ec8c9c27a86228b19a0d43cdc1892a8dd4df0548@ec2-184-73-216-48.compute-1.amazonaws.com:5432/dc4q78egcrbjbr'
    pgres_engine = create_engine(pgres_str)

    # ____ Port sqlite to postgres ___
    run_conversion(pgres_engine)

    # ___ end main ___________

    print('Conversion successful.....')
    return

#  Launched from the command line
if __name__ == '__main__':
    main()
