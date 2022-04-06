# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:10:13 2022

@author: francisco.barros
"""

#!/usr/bin/env python

import argparse
import logging
from midiutil import MIDIFile
import random
import numpy as np
import pygame
import sys
import time
from utils import *

def main(repeats, max_number_of_notes, octave, input_scale):

    for count in range(int(repeats)):
        
        notes = generate_notes(max_number_of_notes,octave,input_scale)
        exercise_ear_training(notes, max_number_of_notes, input_scale)
        play_music()
        time.sleep(8)
        play_music()
        time.sleep(8)
        play_music()
        time.sleep(8)
        print(str(repeats-count)+" exercises to end, nice!")
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Ear training exercise.")
    parser.add_argument(
        'repeats', 
        help='Number of times the exercise will be generated.'
    )
    parser.add_argument(
        'max_number_of_notes', 
        help='Number of notes on phrase.'
    )
    parser.add_argument(
        'octave', 
        help='Octave from each phrase will be generated.'
    )
    parser.add_argument(
        'input_scale', 
        help='Scale from which the phrase will be generated.'
    )
    args = parser.parse_args()
    
    try:
        logging.info("Starting exercise, good luck!")
        main(args.repeats, args.max_number_of_notes, args.octave, args.input_scale)
    
    except Exception as e:
        logging.error("There is a problem within the exercise.")

        