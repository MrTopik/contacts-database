import sqlite3

# Setup 
def setup():
    global conn
    global cursor
    conn = sqlite3.connect("contacts.db") # Creates the file if doesn't exist
    cursor = conn.cursor()

    # Create table if doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)
    conn.commit()

# CRUD Functions

def add_contact(name, phone, email):
    cursor.execute(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email)
    )
    conn.commit()

def get_all_contacts():
    cursor.execute("SELECT * FROM contacts")
    return cursor.fetchall()

def update_contact(contact_id, name, phone, email):
    cursor.execute(
        "UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
        (name, phone, email, contact_id)
    )
    conn.commit()

def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    cursor.execute("SELECT id FROM contacts ORDER BY id")
    remaining = cursor.fetchall()
    for new_id, (old_id,) in enumerate(remaining, start=1):
        if old_id != new_id:
            cursor.execute("UPDATE contacts SET id=? WHERE id=?", (new_id, old_id))
    conn.commit()

def find_contact(name):
    search = name + '%'
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", (search,))
    return cursor.fetchall()

def find_exact(name):
    cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
    return cursor.fetchall()

def find_contact_id(contact_id):
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    return cursor.fetchall()

def close():
    conn.close()