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
import time
from utils import *

def main(repeats, max_number_of_notes, min_midi, max_midi):
    print("aqui")
    for count in range(int(repeats)):
        exercise_ear_training(max_number_of_notes, min_midi, max_midi)
        play_music()
        time.sleep(8)
        play_music()
        time.sleep(8)
        play_music()
        time.sleep(8)
    
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
        'min_midi', 
        help='Lower midi note.'
    )
    parser.add_argument(
        'max_midi', 
        help='Higher midi note.'
    )
    args = parser.parse_args()
    
    #try:
    logging.info("Starting exercise, good luck!")
    main(args.repeats, args.max_number_of_notes, args.min_midi, args.max_midi)
    #except Exception as e:
        #logging.error("There is a problem within the exercise.")

        