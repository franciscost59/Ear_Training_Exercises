# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:00:23 2022

@author: francisco.barros
"""
from midiutil import MIDIFile
import random
import numpy as np
import pygame
import time

file = "./exercise_ear_training.mid"

def play_music():
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
        print("Music file %s loaded!" % file)
    except pygame.error:
        print ("File %s not found! (%s)" % (file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.music.set_volume(0.8)

def exercise_ear_training(max_number_of_notes,min_midi,max_midi):
    """
    This function generates an ear_training exercise

    Parameters
    ----------
    max_number_of_notes : int
        Maximum number of notes on a phrase.
    min_midi : int
        Minimal midi octave.
    max_midi : int
        Max midi octave

    Returns None
    -------

    """
    number_of_notes = random.randint(1,int(max_number_of_notes))
    degrees = []
    track    = 0
    channel  = 0
    time_beats     = 0    # In beats
    duration = 1    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard
    
    for h in range(int(number_of_notes)):
        degrees.append(random.randint(int(min_midi),int(max_midi))) # octave definition c5 60,71

    print("Random notes: ", degrees)
    
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, time_beats, tempo)

    for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, time_beats + i, duration, volume)

    with open("exercise_ear_training.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
        
def play():
    """
    Play midi files

    Returns Mone
 
    """
    file = "./exercise_ear_training.mid"
    play_music(file)
    time.sleep(10)
    play_music(file)
    time.sleep(10)