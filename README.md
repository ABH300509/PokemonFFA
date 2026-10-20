# PokemonFFA
import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

### Create 'Relation_Types' table (Stores: WEAK, RESIST, IMMUNE)
cursor.execute("""
CREATE TABLE Relation_Types (
    relation_name TEXT PRIMARY KEY,
    multiplier REAL NOT NULL
);
""")

### Multiplier Rules
cursor.executemany("""
INSERT INTO Relation_Types (relation_name, multiplier) 
VALUES (?, ?);
""", [
    ('WEAK', 2.0),
    ('RESIST', 0.5),
    ('IMMUNE', 0.0)
])

### Create Types Table
cursor.execute("""
CREATE TABLE Types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE
);
""")

## Insert types
types_list = [('Bug',), ('Dark',), ('Dragon',), ('Electric',), ('Fairy',), ('Fighting',), ('Fire',), ('Flying',), ('Ghost',), ('Grass',), ('Ground',), ('Ice',), ('Normal',), ('Poison',), ('Psychic',), ('Rock',), ('Steel',), ('Water',), ]
cursor.executemany("INSERT INTO Types (type_name) VALUES (?);", types_list)

### Connect two types with a relation tag
cursor.execute("""
CREATE TABLE Type_Relations (
    attacker_type_id INTEGER,
    defender_type_id INTEGER,
    relation_name TEXT NOT NULL,
    PRIMARY KEY (attacker_type_id, defender_type_id),
    FOREIGN KEY (attacker_type_id) REFERENCES Types(type_id),
    FOREIGN KEY (defender_type_id) REFERENCES Types(type_id),
    FOREIGN KEY (relation_name) REFERENCES Relation_Types(relation_name)
);
""")

## Matchup Table (Attacker, Defender, Relation tag)
matchups = [

    ('Fire', 'Bug', 'WEAK'),
    ('Flying', 'Bug', 'WEAK'),
    ('Rock', 'Bug', 'WEAK'),
    ('Fighting', 'Bug', 'RESIST'),
    ('Grass', 'Bug', 'RESIST'),
    ('Ground', 'Bug', 'RESIST'),              
    ('Bug', 'Dark', 'WEAK'),
    ('Fairy', 'Dark', 'WEAK'),
    ('Fighting', 'Dark', 'WEAK'),
    ('Ghost', 'Dark', 'RESIST'),
    ('Dark', 'Dark', 'RESIST'),
    ('Psychic', 'Dark', 'IMMUNE'),
    ('Dragon', 'Dragon', 'WEAK'),
    ('Fairy', 'Dragon', 'WEAK'),
    ('Ice', 'Dragon', 'WEAK'),
    ('Electric', 'Dragon', 'RESIST'),
    ('Fire', 'Dragon', 'RESIST'),
    ('Grass', 'Dragon', 'RESIST'),
    ('Water', 'Dragon', 'RESIST'),
    ('Ground', 'Electric', 'WEAK'),
    ('Electric', 'Electric', 'RESIST'),
    ('Flying', 'Electric', 'RESIST'),
    ('Steel', 'Electric', 'RESIST'),
    ('Poison', 'Fairy', 'WEAK'),
    ('Steel', 'Fairy', 'WEAK'),
    ('Bug', 'Fairy', 'RESIST'),
    ('Dark', 'Fairy', 'RESIST'),
    ('Fighting', 'Fairy', 'RESIST'),
    ('Dragon', 'Fairy', 'IMMUNE'),
    ('Fairy', 'Fighting', 'WEAK'),
    ('Flying', 'Fighting', 'WEAK'),
    ('Psychic', 'Fighting', 'WEAK'),
    ('Bug', 'Fighting', 'RESIST'),
    ('Dark', 'Fighting', 'RESIST'),
    ('Rock', 'Fighting', 'RESIST'),
    ('Ground', 'Fire', 'WEAK'),
    ('Rock', 'Fire', 'WEAK'),
    ('Water', 'Fire', 'WEAK'),
    ('Bug', 'Fire', 'RESIST'),
    ('Fairy', 'Fire', 'RESIST'),
    ('Fire', 'Fire', 'RESIST'),
    ('Grass', 'Fire', 'RESIST'),
    ('Ice', 'Fire', 'RESIST'),
    ('Steel', 'Fire', 'RESIST'),
    ('Electric', 'Flying', 'WEAK'),
    ('Ice', 'Flying', 'WEAK'),
    ('Rock', 'Flying', 'WEAK'),
    ('Bug', 'Flying', 'RESIST'),
    ('Fighting', 'Flying', 'RESIST'),
    ('Grass', 'Flying', 'RESIST'),
    ('Ground', 'Flying', 'IMMUNE'),
    ('Dark', 'Ghost', 'WEAK'),
    ('Ghost', 'Ghost', 'WEAK'),
    ('Bug', 'Ghost', 'RESIST'),
    ('Poison', 'Ghost', 'RESIST'),
    ('Fighting', 'Ghost', 'IMMUNE'),
    ('Normal', 'Ghost', 'IMMUNE'),
    ('Bug', 'Grass', 'WEAK'),
    ('Fire', 'Grass', 'WEAK'),
    ('Flying', 'Grass', 'WEAK'),
    ('Ice', 'Grass', 'WEAK'),
    ('Poison', 'Grass', 'WEAK'),
    ('Electric', 'Grass', 'RESIST'),
    ('Grass', 'Grass', 'RESIST'),
    ('Ground', 'Grass', 'RESIST'),
    ('Water', 'Grass', 'RESIST'),
    ('Grass', 'Ground', 'WEAK'),
    ('Ice', 'Ground', 'WEAK'),
    ('Water', 'Ground', 'WEAK'),
    ('Poison', 'Ground', 'RESIST'),
    ('Rock', 'Ground', 'RESIST'),
    ('Electric', 'Ground', 'IMMUNE'),
    ('Fighting', 'Ice', 'WEAK'),
    ('Fire', 'Ice', 'WEAK'),
    ('Rock', 'Ice', 'WEAK'),
    ('Steel', 'Ice', 'WEAK'),
    ('Ice', 'Ice', 'RESIST'),
    ('Fighting', 'Normal', 'WEAK'),
    ('Ghost', 'Normal', 'IMMUNE'),
    ('Ground', 'Poison', 'WEAK'),
    ('Psychic', 'Poison', 'WEAK'),
    ('Bug', 'Poison', 'RESIST'),
    ('Fairy', 'Poison', 'RESIST'),
    ('Fighting', 'Poison', 'RESIST'),
    ('Grass', 'Poison', 'RESIST'),
    ('Poison', 'Poison', 'RESIST'),
    ('Bug', 'Psychic', 'WEAK'),
    ('Dark', 'Psychic', 'WEAK'),
    ('Ghost', 'Psychic', 'WEAK'),
    ('Fighting', 'Psychic', 'RESIST'),
    ('Psychic', 'Psychic', 'RESIST'),
    ('Fighting', 'Rock', 'WEAK'),
    ('Grass', 'Rock', 'WEAK'),
    ('Ground', 'Rock', 'WEAK'),
    ('Steel', 'Rock', 'WEAK'),
    ('Water', 'Rock', 'WEAK'),
    ('Fire', 'Rock', 'RESIST'),
    ('Flying', 'Rock', 'RESIST'),
    ('Normal', 'Rock', 'RESIST'),
    ('Poison', 'Rock', 'RESIST'),
    ('Fighting', 'Steel', 'WEAK'),
    ('Fire', 'Steel', 'WEAK'),
    ('Ground', 'Steel', 'WEAK'),
    ('Bug', 'Steel', 'RESIST'),
    ('Dragon', 'Steel', 'RESIST'),
    ('Fairy', 'Steel', 'RESIST'),
    ('Flying', 'Steel', 'RESIST'),
    ('Grass', 'Steel', 'RESIST'),
    ('Ice', 'Steel', 'RESIST'),
    ('Normal', 'Steel', 'RESIST'),
    ('Psychic', 'Steel', 'RESIST'),
    ('Rock', 'Steel', 'RESIST'),
    ('Steel', 'Steel', 'RESIST'),
    ('Poison', 'Steel', 'IMMUNE'),
    ('Electric', 'Water', 'WEAK'),
    ('Grass', 'Water', 'WEAK'),
    ('Fire', 'Water', 'RESIST'),
    ('Ice', 'Water', 'RESIST'),
    ('Steel', 'Water', 'RESIST'),
    ('Water', 'Water', 'RESIST'),
]

#### Translate type names into their database IDs
for attacker, defender, relation in matchups:
    cursor.execute("""
    INSERT INTO Type_Relations (attacker_type_id, defender_type_id, relation_name)
    VALUES (
        (SELECT type_id FROM Types WHERE type_name = ?),
        (SELECT type_id FROM Types WHERE type_name = ?),
        ?
    );
    """, (attacker, defender, relation))

conn.commit()


### Get the multiplier between two types
def get_multiplier(attacker_type, defender_type):
    query = """
    SELECT COALESCE(rt.multiplier, 1.0) AS multiplier
    FROM Types atk
    CROSS JOIN Types def
    LEFT JOIN Type_Relations tr 
        ON tr.attacker_type_id = atk.type_id 
       AND tr.defender_type_id = def.type_id
    LEFT JOIN Relation_Types rt 
        ON tr.relation_name = rt.relation_name
    WHERE atk.type_name = ? AND def.type_name = ?;
    """
    cursor.execute(query, (attacker_type, defender_type))
    result = cursor.fetchone()
    return result[0]
