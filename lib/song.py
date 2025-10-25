class Song:
    count = 0
    
    genres = set()
    artists = set()
    
    genre_count = {} 
    artist_count = {} 

    def __init__(self, name: str, artist: str, genre: str):
        self.name = name
        self.artist = artist
        self.genre = genre.strip().capitalize()

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre: str):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist: str):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre: str):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist: str):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
    
    @staticmethod
    def display_all_stats():
        print("-" * 50)
        print("🎶 Global Song Statistics 🎶")
        print("-" * 50)
        
        print(f"Total Songs Created: {Song.count}")
        
        print("\n--- Unique Categories ---")
        print(f"Unique Genres: {sorted(list(Song.genres))}")
        print(f"Unique Artists: {sorted(list(Song.artists))}")
        
        print("\n--- Genre Breakdown (Count) ---")
        print(Song.genre_count)
        
        print("\n--- Artist Responsibility (Count) ---")
        print(Song.artist_count)
        print("-" * 50)

song1 = Song("Running Up That Hill", "Kate Bush", "Pop")
song2 = Song("Bohemian Rhapsody", "Queen", "Rock")
song3 = Song("Sweet Dreams", "Eurythmics", "Pop")
song4 = Song("Purple Haze", "Jimi Hendrix", "Rock")
song5 = Song("Don't Stop Me Now", "Queen", "Rock")
song6 = Song("Shape of You", "Ed Sheeran", "pop")
song7 = Song("The A Team", "Ed Sheeran", "folk")

Song.display_all_stats()

print(f"\nIndividual song check: Song 5 is '{song5.name}' by {song5.artist} in genre {song5.genre}")
