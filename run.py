import os
import argparse
import mido
from mido import Message, MidiFile, MidiTrack


def create_midi_file(filename, repeats=10):
    # Define a dictionary to map instruments to MIDI notes
    note_values = {
        "B": 36,  # Conga Bass
        "O": 37,  # Conga Open
        "S": 38,  # Conga Slap
        "o": 39,  # Bongo Open
        "s": 40,  # Bongo Slap
        "H": 41,  # Closed Hi-hat
        "L": 42,  # Low Tom
        "c": 43,  # Clap
        "m": 44,  # Maracas
        "X": 45,  # High Tom
        "M": 46,  # Open Hi-hat
        "N": 47,  # Low-Mid Tom
        "C": 48,  # High-Mid Tom
        "T": 49,  # Crash Cymbal 1
        "t": 50,  # High Tom 2
        # Add more instruments as needed...
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

    # Create a new MIDI file
    mid = MidiFile()

    # Process each line of the drum pattern
    for line in drum_pattern.strip().split("\n"):
        track = MidiTrack()
        mid.tracks.append(track)

        for _ in range(repeats):
            tick = 0  # Reset tick for each repeat
            for char in line:
                # If the character is a note, add it to the track
                if char in note_values:
                    note = note_values[char]
                    track.append(
                        Message("note_on", note=note, velocity=64, time=tick, channel=9)
                    )
                    tick += 10  # Advance the tick by one note length
                else:
                    tick += 10  # Advance the tick for a rest beat

                # Silence after each note
                track.append(
                    Message("note_off", note=note, velocity=64, time=tick, channel=9)
                )

    # Save the MIDI file
    mid.save(filename)


def play_midi_file(filename):
    # Call timidity to play the midi file
    os.system(f"timidity {filename}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--play", help="Play a midi file", action="store_true")
    parser.add_argument(
        "--repeats", type=int, default=10, help="Number of times to repeat the pattern"
    )
    parser.add_argument("filename", help="The name of the file to play or create")
    args = parser.parse_args()

    if args.play:
        play_midi_file(args.filename)
    else:
        create_midi_file(args.filename, args.repeats)


if __name__ == "__main__":
    main()
