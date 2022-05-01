import duckdb

con = duckdb.connect()

con.execute("CREATE TABLE tbl AS SELECT * FROM read_csv_auto('data.csv', header = True, columns = {'Votes': 'INTEGER', 'Movie': 'String'})")

# def add_vote(movie):
#     result = con.execute("SELECT Vote FROM tbl WHERE Movie == {movie}")
#
#     con.execute("INSERT INTO tbl VALUES (1, 'Jungkook')")
#
# add_vote("gamer")

con.execute("INSERT INTO tbl VALUES (1, 'Jungkook')")

con.execute("COPY tbl TO 'data.csv' (HEADER, DELIMITER ',')")




