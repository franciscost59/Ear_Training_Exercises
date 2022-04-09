# Ear Training Exercises
## Summary

This repository was created to accommodate some ear training exercises. Currently, the program will generate some random musical phrases from either the major scale, minor melodic, major harmonic, minor harmonic and chromatic scales, repeating this random musical phrase three times. The user is able to select the scale from which the phrase will be derived, the number of times the exercises will be repeated, the maximum number of notes a given phrase can have and the octave of a given phrase. A midi map is available inside the folder resources.

## Documentation

Documentation will be provided shortly.

## Repository structure

These repository is organized into two folders *scripts* and *resources*. Scripts contains all the necessary code to run the exercises whereas resources contains the midi map figure.

## Prerequisites

To install the necessary requirements packages for this repository, please run the command below:

```
pip install -r requirements.txt
```

## Running

To run the exercises, please set your directory to the root of the repository and run the next command:

```
python ./scripts/main.py <Number_of_repetitions> <Maximum_number_of_notes_per_phrase> <Octave_range> <Scale_input>
```

**Note:** The scale inputs should be "Major_Scale" or "Minor_Melodic" or "Major_Harmonic" or "Minor_Harmonic" or "Chromatic_Scale". 

An example of the exercises can be ran by executing the following command:

```
python ./scripts/main.py 10 6 4 "Chromatic_Scale"
```