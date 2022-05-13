import duckdb
from api.vote import vote

# load the csv into main memory
con = duckdb.connect()
con.execute("CREATE TABLE tbl AS SELECT * FROM read_csv_auto('data.csv', header = True, columns = {'Votes': 'INTEGER', 'Movie': 'String'})")


vote(con)


# output the database to the csv
con.execute("COPY tbl TO 'data.csv' (HEADER, DELIMITER ',')")




