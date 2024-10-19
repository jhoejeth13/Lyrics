import pygame
import threading
import time

def play_music(start_time):
    pygame.mixer.init()
    pygame.mixer.music.load("Daniel Caesar - Always.mp3")  # Replace with your music file
    pygame.mixer.music.play(start=start_time)

def print_lyrics():
    lyrics = [
        "And I'll be here",
        "'Cause we both know how it goes",
        "I don't want things to change",
        "I pray they stay the same always",
        "And I don't care",
        "If you're with somebody else",
        "I'll give you time and space",
        "Just know I'm not a phase",
        "I'm always, ways, ways",
        "Always, ways, ways",
        "I'm always, ways, ways"
    ]
    
    delay_times = [3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 5] 
    for i, line in enumerate(lyrics):
        sentences = line.split(". ")
        for sentence in sentences:
            print(sentence)
            time.sleep(delay_times[i])

def main():
    start_time = 56  

    music_thread = threading.Thread(target=play_music, args=(start_time,))
    music_thread.start()

    print("\n")
    print_lyrics()

    music_thread.join()

if __name__ == "__main__":
    main()
