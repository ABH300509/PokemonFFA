import sqlite 3

DB_PATH = "pokemon.db"

conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()

def create_pokemon_table(cursor):
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS POKEMON (
      pokemon_id INTEGER PRIMARY KEY AUTOINCREMENT,
      pokemon_name TEXT NOT NULL UNIQUE,
      type1_id INTEGER NOT NULL,
      type2_id INTEGER,
      hp INTEGER NOT NULL,
      atk INTEGER NOT NULL,
      defense INTEGER NOT NULL,
      spatk INTEGER NOT NULL,
      spdf INTEGER NOT NULL,
      speed INTEGER NOT NULL,
      FOREIGN_KEY (type1_id) REFERENCES Types (type_id)
      FOREIGN KEY (type2_id) REFERENCES Types (type_id)
    );
  """)

def insert_pokemon(
  cursor,
  pokemon_name,
  type1_id,
  type2_id,
  hp,
  atk, 
  defense,
  spatk,
  spdf,
  speed
):
cursor.execute("""
  INSERT OR IGNORE INTO Pokemon (
    pokemon_name, type1_id, type2_id, hp, atk, defense, spatk, spdf, speed)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (pokemon_name, type1_id, type2_id, hp, atk, defense, spatk, spdf, speed))

create_pokemon_table(cursor)
conn.commit()
conn.close()
          
