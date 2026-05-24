#import data
import sqlite3

DATABASE = 'music.db'

#Menu
def show_songs():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()

        while True:
            print("1. Search by genre")
            print("2. Search by artist")
            print("3. Search by duration")
            print("4. Exit")

#ask for choice
            choice = input("Choose option: ")

#Ask for specification            
            if choice == "1":
                genre = input("Enter genre: ")
                sql = "SELECT title, artist, duration FROM Music WHERE genre = ?;"
                values = (genre,)

            elif choice == "2":
                artist = input('Enter artist: ')
                sql = "SELECT title, artist, duration FROM Music WHERE artist = ?;"
                values = (artist,)
            
            elif choice == "3":
                try:
                    duration = float(input('Minimum duration: '))
                except:
                    print("Invalid input")
                    continue 
                sql = "SELECT title, artist, duration FROM Music WHERE duration > ?;"
                values = (duration,)

            elif choice == "4":
                print("Exiting program...")
                break

            else:
                print("Invalid choice")
                continue

#print results            
            cursor.execute(sql, values)
            results = cursor.fetchall()

            if not results:
                print("No songs found.")
            else:
                for song in results:
                    print(f"{song[0]} by {song[1]} - {song[2]} min")


if __name__ == "__main__":
    show_songs()
