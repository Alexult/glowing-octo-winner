import numpy as np
import random

def vote(con, name):
    result = con.execute("SELECT Votes FROM tbl WHERE Movie == ?", [name]).fetchnumpy()
    votes = result['Votes']

    if np.size(votes) == 0:
        con.execute("INSERT INTO tbl VALUES (?, ?)", [1, name])
    else:
        con.execute("UPDATE tbl SET Votes = ? WHERE Movie == ? ", [votes[0].item() + 1, name])


def removeFirst(con):
    result = con.execute("SELECT Movie FROM tbl WHERE Votes = (SELECT MAX(Votes) FROM tbl)").fetchnumpy()
    if np.size(result['Movie']) == 0:
        return False
    size = np.size(result['Movie'])
    rand = np.floor(size * random.random())
    movie = result['Movie'][int(rand.item())]
    con.execute("DELETE FROM tbl WHERE Movie == ?", [movie])
    return movie