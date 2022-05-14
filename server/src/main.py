import duckdb
import api

# load the csv into main memory
con = duckdb.connect()
con.execute("CREATE TABLE tbl AS SELECT * FROM read_csv_auto('data.csv', header = True, columns = {'Votes': 'INTEGER', 'Movie': 'String'})")


api.vote(con, "Jungkook")
api.vote(con, "Junkook")


# output the database to the csv
con.execute("COPY tbl TO 'data.csv' (HEADER, DELIMITER ',')")
con.close()




