import duckdb
import api

# load the csv into main memory
con = duckdb.connect()
con.execute("CREATE TABLE tbl AS SELECT * FROM read_csv_auto('data.csv', header = True, columns = {'Votes': 'INTEGER', 'Movie': 'String'})")

while True:
    print("Please choose an option:\n1:vote\n2:return the next movie\n3:quit")
    option = input()
    if option == "1":
        print("What movie do you want to vote for?")
        movie = input()
        api.vote(con, movie)
        print("You have successfully voted for" + movie)
    elif option == "2":
        result = api.removeFirst(con)
        if result == False:
            print("there are no movies in the waiting list :(")
        else:
            print("The next movie we should watch is " + result)
    elif option == "3":
        con.execute("COPY tbl TO 'data.csv' (HEADER, DELIMITER ',')")
        con.close()
        break
    else:
        print("invalid input")

