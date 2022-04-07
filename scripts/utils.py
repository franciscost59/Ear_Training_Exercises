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
import logging
import sys

file = "./exercise_ear_training.mid"

def play_music():
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
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

def generate_notes(max_number_of_notes,octave,input_scale):
    
    first_note = 12*int(octave)
    last_note = 12*int(octave)+12
    generate_octave = np.arange(first_note,last_note)
    print(generate_octave)
    major_scale = [0,2,4,5,7,9,11]
    minor_melodic = [0,2,3,5,7,9,11]
    major_harmonic = [0,2,4,5,7,8,11]
    minor_harmonic = [0,2,3,5,7,8,11]
    chromatic_scale = generate_octave
    
    if input_scale == "Major_Scale":
        notes = generate_octave[major_scale]
    elif input_scale == "Minor_Melodic":
        notes = generate_octave[minor_melodic]
    elif input_scale == "Major Harmonic":
        notes = generate_octave[major_harmonic]
    elif input_scale == "Minor Harmonic":
        notes = generate_octave[minor_harmonic]
    elif input_scale == "Chromatic_Scale":
        notes = chromatic_scale
    else:
        logging.info("Please select a scale from the list: Major_Scale,Minor_Melodic, Major Harmonic, Minor Harmonic or Chromatic_Scale ")
        exit()
        
    return(notes)

def exercise_ear_training(notes, max_number_of_notes, input_scale):

    number_of_notes = random.randint(1,int(max_number_of_notes))
    
    playback = []
    
    if input_scale != "Chromatic_Scale":
        for r in range(int(max_number_of_notes)):
            playback.append(notes[random.randint(0,6)])
    else:
        for r in range(int(max_number_of_notes)):
            playback.append(notes[random.randint(0,10)])
            
    track    = 0
    channel  = 0
    time_beats     = 0    # In beats
    duration = 1    # In beats
    tempo    = 60   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard

    print("Random notes: ", playback)
    
    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
    MyMIDI.addTempo(track, time_beats, tempo)

    for i, pitch in enumerate(playback):
        MyMIDI.addNote(track, channel, pitch, time_beats + i, duration, volume)

    with open("exercise_ear_training.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
        