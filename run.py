import mido
from mido import Message, MidiFile, MidiTrack

# Define a dictionary to map instruments to MIDI notes
note_values = {
    "B": 36,  # Conga Bass
    "O": 37,  # Conga Open
    "S": 38,  # Conga Slap
    "o": 39,  # Bongo Open
    "s": 40,  # Bongo Slap
    # ... You'll need to fill in the rest ...
}

# Define the drum pattern
drum_pattern = """
B---O---O-S---O---O-S---
---o---s---o---s---o---s---
H---L---c-m-c-m-H---L---c-m-
----X-------X-------X-------
L---S---L---S---L---S---L---
M-M-M-M-M-M-M-M-M-M-M-M-M-M-
N-------N-------N-------N---
--------C---------------C---
----T---------------T-------
--------t---------------t---
"""

# Create a new MIDI file with a single track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Process each line of the drum pattern
for line in drum_pattern.strip().split("\n"):
    # Process each character in the line
    for char in line:
        # If the character is a note, add it to the track
        if char in note_values:
            note = note_values[char]
            track.append(Message("note_on", note=note, velocity=64, time=0))
            track.append(
                Message("note_off", note=note, velocity=64, time=480)
            )  # 480 ticks is a quarter note in MIDI, you may need to adjust this

# Save the MIDI file
mid.save("drum_pattern.mid")
import os
import argparse
import mido
from mido import Message, MidiFile, MidiTrack


def create_midi_file(filename):
    # Define a dictionary to map instruments to MIDI notes
    note_values = {
        "B": 36,  # Conga Bass
        "O": 37,  # Conga Open
        "S": 38,  # Conga Slap
        "o": 39,  # Bongo Open
        "s": 40,  # Bongo Slap
        # ... You'll need to fill in the rest ...
    }

    # Define the drum pattern
    drum_pattern = """
    B---O---O-S---O---O-S---
    ---o---s---o---s---o---s---
    H---L---c-m-c-m-H---L---c-m-
    ----X-------X-------X-------
    L---S---L---S---L---S---L---
    M-M-M-M-M-M-M-M-M-M-M-M-M-M-
    N-------N-------N-------N---
    --------C---------------C---
    ----T---------------T-------
    --------t---------------t---
    """

    # Create a new MIDI file with a single track
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Process each line of the drum pattern
    for line in drum_pattern.strip().split("\n"):
        # Process each character in the line
        for char in line:
            # If the character is a note, add it to the track
            if char in note_values:
                note = note_values[char]
                track.append(Message("note_on", note=note, velocity=64, time=0))
                track.append(
                    Message("note_off", note=note, velocity=64, time=480)
                )  # 480 ticks is a quarter note in MIDI, you may need to adjust this

    # Save the MIDI file
    mid.save(filename)


def play_midi_file(filename):
    # Call timidity to play the midi file
    os.system(f"timidity {filename}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--play", help="Play a midi file", action="store_true")
    parser.add_argument("filename", help="The name of the file to play or create")
    args = parser.parse_args()

    if args.play:
        play_midi_file(args.filename)
    else:
        create_midi_file(args.filename)


if __name__ == "__main__":
    main()
