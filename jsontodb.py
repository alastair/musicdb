import psycopg2
import json
import os
import sys

conn = psycopg2.connect("dbname=musicdb")

def import_file(root, filename):
    doc = open(filename).read()
    filename = filename[len(root)+1:]
    print filename
    cur = conn.cursor()
    query = """insert into audio (path, data) values (%s, %s)"""
    cur.execute(query, (filename, doc))
    conn.commit()

def main(thedir):
    for root, dirs, files in os.walk(thedir):
        for f in files:
            import_file(thedir, os.path.join(root, f))

if __name__ == "__main__":
    main(sys.argv[1])
