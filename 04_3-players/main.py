import sqlite3
import itertools

from datetime import datetime
from uuid import uuid4
from contextlib import closing

dbname = "other-3.db"

def sep(a, b):
  g = a if a > b else b
  l = b if a == g else a
  return (g, l)

with closing(sqlite3.connect(dbname)) as conn:
  c = conn.cursor()
  c.execute("create table list(id text, a1 int, a2 int, b1 int, b2 int, c1 int, c2 int)")

  sql = "insert into list values (?, ?, ?, ?, ?, ?, ?)"
  
  for a1, a2 in itertools.combinations(range(45), 2):
    print("[{2}] {0:02d}-{1:02d}".format(a1, a2, datetime.now()))

    for b1, b2 in itertools.combinations(range(43), 2):
      for c1, c2 in itertools.combinations(range(41), 2):
        ag, al = sep(a1, a2)
        bg, bl = sep(b1, b2)
        cg, cl = sep(c1, c2)
        id = str(uuid4())
        data = (id, ag, al, bg, bl, cg, cl)
        c.execute(sql, data)
  conn.commit()