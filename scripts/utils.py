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
    elif input_scale == "Major_Harmonic":
        notes = generate_octave[major_harmonic]
    elif input_scale == "Minor_Harmonic":
        notes = generate_octave[minor_harmonic]
    elif input_scale == "Chromatic_Scale":
        notes = chromatic_scale
    else:
        logging.info("Please select a scale from the list: Major_Scale,Minor_Melodic, Major_Harmonic, Minor_Harmonic or Chromatic_Scale ")
        sys.exit()
        
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
    
    return(playback)
        
def verify_result(notes_input):
    
    if abs(notes_input[0]-notes_input[1]) == 0:
        print("Unison")
    if abs(notes_input[0]-notes_input[1]) == 1:
        print("Minor Second")
    if abs(notes_input[0]-notes_input[1]) == 2:
        print("Major Second")
    if abs(notes_input[0]-notes_input[1]) == 3:
        print("Minor Third")
    if abs(notes_input[0]-notes_input[1]) == 4:
        print("Major Thrid")
    if abs(notes_input[0]-notes_input[1]) == 5:
        print("Perfect Fourth")
    if abs(notes_input[0]-notes_input[1]) == 6:
        print("Diminished Fith")
    if abs(notes_input[0]-notes_input[1]) == 7:
        print("Perfect Fifth")
    if abs(notes_input[0]-notes_input[1]) == 8:
        print("Minor Sixth")
    if abs(notes_input[0]-notes_input[1]) == 9:
        print("Major Sixth")
    if abs(notes_input[0]-notes_input[1]) == 10:
        print("Minor Seventh")
    if abs(notes_input[0]-notes_input[1]) == 11:
        print("Major Seventh")
    if abs(notes_input[0]-notes_input[1]) == 12:
        print("Perfect Octave")
    else:
        return None
        
        
        
        
        