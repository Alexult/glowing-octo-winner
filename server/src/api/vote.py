import duckdb
import numpy as np


def vote(con, name):
    result = con.execute("SELECT Votes FROM tbl WHERE Movie == ?", [name]).fetchnumpy()
    votes = result['Votes']

    if np.size(votes) == 0:
        con.execute("INSERT INTO tbl VALUES (?, ?)", [1, name])
    else:
        con.execute("UPDATE tbl SET Votes = ? WHERE Movie == ? ", (votes[0].item() + 1, name))
