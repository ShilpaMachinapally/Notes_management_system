from database.connection import database_config, cursor

def create_tables():
    users_table_query = """
        CREATE TABLE IF NOT EXISTS USERS(
        USERID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERNAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL UNIQUE,
        PASSWORD TEXT
        );
    """

    notes_table_query = """
        CREATE TABLE IF NOT EXISTS NOTES (
        NOTEID INTEGER PRIMARY KEY AUTOINCREMENT,
        USERID INTEGER NOT NULL,
        EMAIL TEXT NOT NULL,
        TITLE TEXT NOT NULL,
        CONTENT TEXT,
        LAST_UPDATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (USERID) REFERENCES USERS(USERID)
            ON DELETE CASCADE
        );
    """

    cursor.execute(users_table_query)
    cursor.execute(notes_table_query)

    database_config.commit()   # ✅ VERY IMPORTANT

    print("tables created successfully")