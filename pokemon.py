import sqlite3

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

def insert_pokemon(cursor, data):
    cursor.executemany("""
        INSERT OR IGNORE INTO Pokemon (
            pokemon_name,
            type1_id,
            type2_id,
            hp,
            atk,
            defense,
            spatk,
            spdf,
            speed
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

create_pokemon_table(cursor)
POKEMON_DATA = [
  ("Venusaur", 10, 14, 80, 82, 83, 100, 100, 80),
  ("Charizard", 7, 8, 78, 84, 78, 109, 85, 100),
  ("Blastoise", 18, None, 79, 83, 100, 85, 105, 78),
  ("Mew", 15, None, 100, 100, 100, 100, 100, 100), 
  ("Mewtwo", 15, None, 106, 110, 90, 154, 90, 130),
  ("Zapdos", 4, 8, 90, 90, 85, 125, 90, 100),
  ("Moltres", 7, 8, 90, 100, 90, 125, 85, 90),
  ("Articuno", 12, 8, 90, 85, 100, 95, 125, 85),
  ("Pidgeot", 13, 8, 83, 80, 75, 70, 70, 101),
  ("Arbok", 14, None, 60, 95, 69, 65, 79, 80),
  ("Pikachu", 4, None, 35, 55, 40, 50, 50, 90),
  ("Pikachu-Ash", 4, None, 35, 160, 40, 150, 50, 90),
  ("Raichu", 4, None, 60, 90, 55, 90, 80, 110),
  ("Nidoqueen", 11, 14, 90, 92, 87, 75, 85, 76),
  ("Nidoking", 11, 14, 81, 102, 77, 85, 75, 85),
  ("Vileplume", 10, 14, 75, 80, 85, 110, 90, 50),
  ("Arcanine", 7, None, 90, 110, 80, 100, 80, 95),
  ("Poliwrath", 18, 6, 90, 95, 95, 70, 90, 70),
  ("Alakazam", 15, None, 55, 50, 45, 135, 95, 120),
  ("Machamp", 6, None, 90, 130, 80, 65, 85, 55),
  ("Golem", 16, 10, 80, 120, 130, 55, 65, 45),
  ("Rapidash", 7, None, 65, 100, 70, 80, 80, 105),
  ("Slowbro", 18, 15, 95, 75, 110, 100, 80, 30),
  ("Magnezone", 17, 4, 70, 70, 115, 130, 90, 60),
  ("Cloyster", 18, 12, 50, 95, 180, 85, 45, 70),
  ("Gengar", 15, 9, 60, 65, 60, 130, 75, 110),
  ("Genesect", 1, 17, 71, 120, 95, 120, 95, 99),
  ("Genesect-Burn", 1, 7, 71, 120, 95, 120, 95, 99),
  ("Genesect-Chill", 1, 12, 71, 120, 95, 120, 95, 99),
  ("Genesect-Douse", 1, 18, 71, 120, 95, 120, 95, 99),
  ("Genesect-Shock", 1, 4, 71, 120, 95, 120, 95, 99),
  ("Steelix", 17, 11, 75, 85, 200, 55, 65, 30),
  ("Kingler", 18, None, 55, 130, 115, 50, 50, 75),
  ("Electrode", 4, None, 60, 70, 70, 80, 80, 150),
  ("Exeggutor", 10, 15, 95, 95, 85, 125, 75, 55),
  ("Marowak", 11, None, 60, 80, 100, 50, 90, 45),
  ("Hitmonlee", 6, None, 50, 120, 53, 35, 110, 87),
  ("Hitmonchan", 6, None, 50, 105, 79, 35, 110, 76),
  ("Hitmontop", 6, None, 50, 95, 95, 35, 110, 70),
  ("Weezing", 14, None, 65, 90, 120, 85, 70, 60),
  ("Rhyperior", 11, 16, 115, 140, 130, 55, 55, 40),
  ("Blissey", 13, None, 255, 10, 10, 75, 135, 55),
  ("Kingdra", 18, 3, 100, 135, 120, 60, 85, 50),
  ("Starmie", 18, 15, 60, 75, 85, 100, 85, 115),
  ("Scyther", 1, 8, 70, 110, 80, 55, 80, 105),
  ("Scizor", 17, 1, 70, 130, 100, 55, 80, 65),
  ("Electivire", 4, 6, 75, 123, 67, 95, 85, 85),
  ("Magmortar", 7, None, 75, 95, 67, 125, 95, 83),
  ("Mr. Mime", 15, 5, 40, 45, 65, 100, 120, 90),
  ("Tauros", 13, None, 75, 100, 95, 40, 70, 110),
  ("Magikarp", 18, None, 20, 10, 55, 15, 20, 80),
  ("Gyarados", 18, 3, 95, 125, 79, 60, 100, 81),
  ("Lapras", 18, 12, 130, 85, 80, 85, 95, 60),
  ("Vaporeon", 18, None, 130, 65, 60, 110, 95, 65),
  ("Flareon", 7, None, 65, 130, 60, 95, 110, 65),
  ("Jolteon", 4, None, 65, 65, 60, 110, 95, 130),
  ("Omastar", 16, 18, 70, 60, 125, 115, 70, 55),
  ("Kabutops", 16, 18, 60, 115, 105, 65, 70, 80),
  ("Aerodactyl", 16, 8, 80, 105, 65, 60, 75, 130),
  ("Snorlax", 13, None, 160, 110, 65, 65, 110, 30),
  ("Dragonite", 3, 8, 91, 134, 95, 100, 100, 80),
] 
insert_pokemon(cursor, POKEMON_DATA)
conn.commit()
conn.close()
          
