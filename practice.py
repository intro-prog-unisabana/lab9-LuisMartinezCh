from song import Song

def print_songs(song_list):
    """
    Recibe una lista de objetos Song e imprime cada uno.
    """
    for song in song_list:
        print(song)

# Bloque de prueba
if __name__ == "__main__":
    songs = [
        Song("tv off", "Kendrick Lamar", 3.7),
        Song("Alright", "Kendrick Lamar", 3.5)
    ]
    
    print_songs(songs)