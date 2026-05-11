import sqlite3

DATABASE = 'music.db'

def show_songs():
    try:
        user_input = float(input('Minimum duration: '))
    except:
        print("Invalid input")
        return 
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()

        sql = "SELECT title, artist, duration FROM Music WHERE duration > ?;"
        cursor.execute(sql, (user_input,))

        results = cursor.fetchall()

        for song in results:
            print(f"{song[0]} by {song[1]} - {song[2]} min")

if __name__ == "__main__":
    show_songs()

