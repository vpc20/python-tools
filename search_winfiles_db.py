import os
import sqlite3


def query_winfile_wildcard(filename_pattern):
    # Connect to the database
    filename_pattern = filename_pattern.replace('*', '%').lower()
    conn = sqlite3.connect('winfiles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Query the winfiles table using a wildcard pattern for the filename
    cursor.execute('''
    SELECT filename, filepath
    FROM winfiles
    WHERE LOWER(filename) LIKE ?
    ''', (filename_pattern,))

    # Fetch all matching rows
    rows = cursor.fetchall()
    for filename, filepath in rows:
        print(f"{filepath}\\{filename}")

    # Close the connection
    conn.close()

    # Return the results
    # return rows


def query_winfile(filename):
    # Connect to the database
    conn = sqlite3.connect('winfiles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Query the winfiles table for the given filename
    cursor.execute('''
    SELECT filepath
    FROM winfiles
    WHERE filename = ?
    ''', (filename,))

    result = cursor.fetchone()

    # Close the connection
    conn.close()

    if result:
        print(f"Filename '{result[0]}' not found in the database.")
    else:
        print(f"Filename '{filename}' not found in the database.")


def delete_all_winfiles():
    # Connect to the database
    conn = sqlite3.connect('winfiles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Delete all records from the winfiles table
    cursor.execute('''
    DELETE FROM winfiles
    ''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    print("All records have been deleted from the winfiles table.")


def print_all_winfiles():
    # Connect to the database
    conn = sqlite3.connect('winfiles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Query to select all rows and columns from the winfiles table
    cursor.execute('''
    SELECT * FROM winfiles
    ''')

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the column names
    column_names = [description[0] for description in cursor.description]
    print(" | ".join(column_names))
    print("-" * 50)

    # Print all rows
    for row in rows:
        print(" | ".join(map(str, row)))

    # Close the connection
    conn.close()


def insert_winfile(folder):
    # Connect to the database
    conn = sqlite3.connect('winfiles.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    ctr = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        if '\\.' in dirpath or 'AndroidStudioProjects' in dirpath:
            print(dirpath)
            continue
        for filename in filenames:
            try:
                cursor.execute('''
                INSERT INTO winfiles (filename, filepath)
                VALUES (?, ?)
                ''', (filename, dirpath))
                ctr += 1
                print(ctr)
            except sqlite3.IntegrityError:
                pass
            # print(filename, dirpath)
            # Commit the changes and close the connection
            conn.commit()

    conn.close()


def create_winfiles_db():
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('winfiles.db')
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    # Create the winfiles table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS winfiles (
    filename TEXT PRIMARY KEY,
    filepath TEXT NOT NULL)
    ''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    print("Table 'winfiles' created successfully.")


if __name__ == '__main__':
    # create_winfiles_db()

    # xxxdelete_all_winfiles()xxx

    # insert_winfile(r'C:\Users\vpc\OneDrive\Documents')
    # insert_winfile(r'C:\Users\vpc\PycharmProjects')
    # insert_winfile(r'C:\Users\vpc')

    # print_all_winfiles()
    # query_winfile('dir2a')
    query_winfile_wildcard('matrix*')
