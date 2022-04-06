# Ear Training Exercises
## Summary

This repository was created to accommodate some ear training exercises. Currently, the program will generate some random musical phrases from the chromatic scale three times. The user is able to select the number of times the exercises will be repeated, the maximum number of a given phrase and the lower and upper pitch (in midi notation) of a given phrase. A midi map is available inside the folder resources.

## Documentation

Documentation will be provided shortly.

## Repository structure

These repository is organized into two folders *scripts* and *resources*. Scripts contains all the necessary code to run the exercises whereas resources contains the midi map figure.

## Prerequisites

There are essential to main requirements to run this repository. First, one needs to install *MIDIUtil* by following the guidelines presented [here](https://github.com/MarkCWirt/MIDIUtil).

Next, one need to install the requirements packages necessary. This can be achieved by running the following command:

```
pip install -r requirements.txt
```

## Running

To run the exercises, please set your directory to the root of the repository and run the next command:

```
python ./scripts/main.py <Number_of_repetitions> <Maximum_number_of_notes_per_phrase> <Lower_midi_pitch> <Upper_midi_pitch>
```

