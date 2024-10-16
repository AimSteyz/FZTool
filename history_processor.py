import sqlite3

def process_history_file(input_file):
    output = []
    output.append("\nBrowser History:")
    output.append("=" * 50)

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(input_file)
        cursor = conn.cursor()

        # Check if the database is corrupted
        cursor.execute("PRAGMA integrity_check;")
        result = cursor.fetchone()
        if result[0] != 'ok':
            return f"Database integrity check failed: {result[0]}"

        # Query the URLs table to get the browser history data
        cursor.execute("SELECT url, title, visit_count FROM urls")

        # Fetch all results and process each row
        rows = cursor.fetchall()

        for row in rows:
            url = row[0]
            title = row[1] if row[1] else "No Title"
            visit_count = row[2]

            # Log the entry to the output (instead of writing to a file)
            output.append(f"Title: {title}")
            output.append(f"URL: {url}")
            output.append(f"Visit Count: {visit_count}")
            output.append("-" * 50)

        # Close the connection
        conn.close()

        # Return the formatted content as a single string
        return "\n".join(output)

    except sqlite3.DatabaseError as e:
        return f"Error processing the SQLite file: {e}"
