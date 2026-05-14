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

        sql = "SELECT * FROM Music WHERE duration > ?;"
        cursor.execute(sql, (user_input,))

        results = cursor.fetchall()

        for song in results:
            print(f"{song[0]} by {song[1]} - {song[2]} min")


def show_songs():
    genre = input('Enter genre: ')

        sql = "SELECT * FROM Music WHERE genre = ?;"
        cursor.execute(sql, (genre,))

        results = cursor.fetchall()

        if not results:
            print("No songs found.")
        else:
            for song in results:
                print(f"{song[1]} by {song[2]} - {song[5]} min")


def show_songs():
    artist = input('Enter artist: ')

        sql = "SELECT * FROM Music WHERE artist = ?;"
        cursor.execute(sql, (artist,))

        results = cursor.fetchall()

        if not results:
            print("No songs found.")
        else:
            for song in results:
                print(f"{song[1]} by {song[2]} - {song[5]} min")

if __name__ == "__main__":
    show_songs()
    