Random midi beat generator, uses plaintext notation as input. Seeds to control
randomness. Outputs .mid, then generates an .ogg sample with arbitrary loop
length (using default instrument voices from timidity.)

Install: 

- brew install timidity
- install poetry, then `poetry init` 

Example usage:

poetry run python3 run.py --repeats 10 --pattern_seed 888 --voice_seed 456
candido008.mid 

This generates the midi file based on the seed.

Then to play it: 

poetry run python3 run.py --play candido008.mid