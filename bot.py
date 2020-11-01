from music import *
from mario import *

'''
    ========================================= WELCOME ===========================================
 this is a bot who plays piano, type song. and use the notes C, C#, D, D#, E, F, F#, G, G#, A, A# and B
 to make your own song (type capital letters). To use the sharp notes, put a 's' before the note's name, example: sC, sD
 you can use the song.breaktime() function to put some seconds of break in your song
 as default it comes with super mario's theme but you can build your own song, type your song in the music area.
 I don't know how to play 2 notes at same time so I made a alternative way to do it, when you type your note you can type
 a "y" after the note's number to play for a long time, example:  C(2, "y") this note will play for a longer time
 I hope you enjoy my little project :).
 '''

"""special effects"""
song = music
song.buttons()
mario = mario()


'''========================================== MUSIC AREA =============================================
type your song here'''
mario.mariosSong()

'''execute the song'''
song.run()
print('done')

'''quit the program'''
time.sleep(3)
song.quit()
