import sqlite3
import itertools

from uuid import uuid4
from contextlib import closing

dbname = "other-2.db"

def sep(a, b):
  g = a if a > b else b
  l = b if a == g else a
  return (g, l)

with closing(sqlite3.connect(dbname)) as conn:
  c = conn.cursor()
  c.execute("create table list(id text, a1 int, a2 int, b1 int, b2 int)")

  sql = "insert into list(id, a1, a2, b1, b2) values (?, ?, ?, ?, ?)"
  
  for a1, a2 in itertools.combinations(range(45), 2):
    for b1, b2 in itertools.combinations(range(43), 2):
      ag, al = sep(a1, a2)
      bg, bl = sep(b1, b2)
      id = str(uuid4())
      data = (id, ag, al, bg, bl)
      c.execute(sql, data)
  conn.commit()