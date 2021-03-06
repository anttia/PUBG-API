import sqlite3

def connect_db():
    return sqlite3.connect('pubg.db')

def init_db(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS matches(id INTEGER PRIMARY KEY, match_id TEXT UNIQUE, rank INTEGER, kills INTEGER);''')

def get_match_by_id(conn, match_id):
    cur = conn.execute("SELECT match_id, rank, kills FROM matches WHERE match_id=?", [match_id])
    record = cur.fetchone()
    if record:
        return {
            "matchId": record[0],
            "rank": record[1],
            "kills": record[2]
        }
    else:
        return None

def create_match_record(conn, record):
    conn.execute("INSERT INTO matches (match_id, rank, kills) VALUES (?,?,?);", (
        record["matchId"],
        record["winPlace"],
        record["kills"]
    ))
    conn.commit()