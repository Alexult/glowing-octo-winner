import duckdb
import numpy as np

def vote(con, name):
    result = con.execute("SELECT Votes FROM tbl WHERE Movie == ?", [name]).fetchnumpy()
    votes = result['Votes'][0] + 1

    con.execute("UPDATE tbl SET Votes = ? WHERE Movie == ? ", (votes.item(), name))