from pygame import mixer

class Music:

    def __init__(self) -> None:
        mixer.init()

        # Loading the song
        mixer.music.load("Assets/Sounds/Musics/Village Horon.mp3")
        
        # Setting the volume
        mixer.music.set_volume(0.5)

        # mixer.music.play(-1)