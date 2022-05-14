import duckdb
import api

# load the csv into main memory
con = duckdb.connect()
con.execute("CREATE TABLE tbl AS SELECT * FROM read_csv_auto('data.csv', header = True, columns = {'Votes': 'INTEGER', 'Movie': 'String'})")

while True:
    print("Please choose an option:\n1:vote\n2:quit")
    option = input()
    if option == "1":
        print("You have chosen to vote for jungkookc")
        api.vote(con, "Jungkook")
    elif option == "2":
        con.execute("COPY tbl TO 'data.csv' (HEADER, DELIMITER ',')")
        con.close()
        break
    else:
        print("invalid input")

