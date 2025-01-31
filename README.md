🎶🎼Music Generation App

**Overview**

The Music Generation App utilizes a Genetic Algorithm to create unique musical sequences based on user feedback. The system evolves melodies over multiple generations, optimizing them using a fitness function that rates melodies based on user input. The generated melodies can be saved as MIDI files and played back using a synthesizer.

**Features**

  - Genetic Algorithm for Melody Generation

  - MIDI File Export

  - Real-Time Playback with Pyo Audio Library

  - Interactive User Rating System

**Dependencies**

Ensure you have the following dependencies installed:

```pip install click midiutil pyo```
**Code Structure**

**1. genetic.py**

    Contains the implementation of the genetic algorithm, including:
    
    Genome Representation: Encodes melodies as binary strings.
    
    Selection, Crossover, and Mutation: Implements single-point crossover and mutation.
    
    Fitness Function: Evaluates melodies based on user input.
    
    Evolution Process: Generates, selects, and optimizes melodies over multiple generations.

**2. mgen.py**
    
    Handles melody generation and playback, including:
    
    Melody Representation: Converts genomes into musical notes.
    
    Event Sequences: Uses Pyo for audio playback.
    
    User Rating System: Allows user input to guide evolution.
    
    MIDI Export: Saves generated melodies to MIDI files.

How to Run

Generate and Evolve Music:

python mgen.py

Rate Melodies to Improve Evolution: After playback, input a rating (0-5) to guide optimization.

Save to MIDI: Export generated melodies for further use.
