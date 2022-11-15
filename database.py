import sqlite3
from typing import List
import datetime
from model import Extension

conn = sqlite3.connect('extensions.db')
c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS extensions (
            name text,
            version text,
            url text,
            date_added text
            )""")


create_table()


def insert_ext(ext: Extension):
    c.execute('select count(*) FROM extensions')
    with conn:
        c.execute('INSERT INTO extensions VALUES (:name, :version, :url, :date_added)',
        {'name': ext.name, 'version': ext.version, 'url': ext.url, 'date_added': ext.date_added,})


def get_all_ext() -> List[Extension]:
    c.execute('select * from extensions')
    results = c.fetchall()
    extensions = []
    for result in results:
        extensions.append(Extension(*result))
    return extensions
