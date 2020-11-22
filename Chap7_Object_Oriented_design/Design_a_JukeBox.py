# Jukebox: Design a musical Jukebox using object oreinted principles
# Questions: 
    # is the jukebox playing CDs? Records? MP3s? is it a simulation on a computer or
    #is it supposed to represent a physical jukebox?
    # Does it take money or is it free ? Which currency ?
    # Does it deliver change ? 

    # Assumptions: 
        # The jukebox is a computer simulation that closesly mirrors physical jukeboxes
        # and we will assume that it is free


class Jukebox(object): # why do I need to include object 
    def __init__(self, songs):
        self.songs = {}
        for song in songs: 
            self.songs[song.title] = song
        self.playing = None

    def play_song(self, title):
        if self.playing:
            self.stop_song()
        self.playing = self.songs[title]
        self.playing.play()


    def stop_song(self):
        if self.playing:
            self.playing.stop() #  should this be self.stop ?

    def stop_song(self):
        if self.playing:
            self.playing.stop()

    class Song(object): # why do I need to include object 
        def __init__(self, title, data):
            self.title, self.data = tile, data 
            self.play_count = 0 

        def play(self):
            self.is_playing = True
            self.play_count += 1

        def stop(self):
            self.playing = False


