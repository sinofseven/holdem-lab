import sqlite3
import itertools

from uuid import uuid4
from contextlib import closing

dbname = "other-1.db"

with closing(sqlite3.connect(dbname)) as conn:
  c = conn.cursor()
  c.execute("create table list(id text, a1 int, a2 int)")

  sql = "insert into list(id, a1, a2) values (?, ?, ?)"
  
  for one, two in itertools.combinations(range(45), 2):
    greater = one if one > two else two
    less = two if greater == one else one
    id = str(uuid4())
    data = (id, greater, less)
    c.execute(sql, data)
  conn.commit()