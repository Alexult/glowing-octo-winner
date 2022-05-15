import duckdb
import numpy as np
from flask import Flask

app = Flask(__name__)

# load the csv into main memory
con = duckdb.connect()
con.execute("""
    CREATE TABLE tbl AS SELECT *
    FROM read_csv_auto('data.csv', header = True, columns = {'Votes': 'INTEGER', 'Movie': 'String'})
    """)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/1')
def vote(con, name):
    """
    Adds a vote to the database for that movie. If the movie isn't in the database yet it is added
    :param con: connection to the database
    :param name: the name of the movie to vote on
    :return: returns the amount of votes the movie has now
    """
    result = con.execute("SELECT Votes FROM tbl WHERE Movie == ?", [name]).fetchnumpy()
    votes = result['Votes']

    if np.size(votes) == 0:
        con.execute("INSERT INTO tbl VALUES (?, ?)", [1, name])
        return 1
    con.execute("UPDATE tbl SET Votes = ? WHERE Movie == ? ", [votes[0].item() + 1, name])
    return votes[0].item() + 1


def removeFirst(con):
    """
    removes the movie with the most votes and returns it
    :param con: the connection to the database
    :return: returns the movie that was removed and false if there is no eligible movie
    """
    result = con.execute("SELECT Movie FROM tbl ORDER BY Votes DESC LIMIT 1").fetchnumpy()
    if np.size(result['Movie']) == 0:
        return False
    movie = result['Movie'][0]
    con.execute("DELETE FROM tbl WHERE Movie == ?", [movie])
    return movie
