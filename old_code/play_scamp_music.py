# play_AI_music.py 
from scamp import *

s = Session(tempo=120)
clar = s.new_part("clarinet", 0)

def load_note_variables():
    with open("notes.txt", "r") as file:
        for line in file.readlines():
            name, value = line.strip().split(" = ")
            globals()[name] = int(value)

load_note_variables()

melody = [
    (C4, 1/4), (D4, 1/4), (E4, 1/4), (F4, 1/4),
    (G4, 1/4), (A4, 1/4), (B4, 1/4), (C5, 1/4),
    (B4, 1/4), (A4, 1/4), (G4, 1), (F4, 1)
]

for pitch, duration in melody:
    clar.play_note(pitch, 0.7, duration)

print("Melody completed!")

# Someday maybe transcription?