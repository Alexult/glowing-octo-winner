import duckdb

def vote(con):
    con.execute("INSERT INTO tbl VALUES (1, 'Jungkook')")