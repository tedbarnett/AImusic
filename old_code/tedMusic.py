from requests import Session
from scamp import *

s = Session(tempo=120)
clar = s.new_part("clarinet", 0)
s.start_transcribing()

# Load MIDI note names & numbers from notes.txt
def load_note_variables():
    with open("notes.txt", "r") as file:
        for line in file.readlines():
            name, value = line.strip().split(" = ")
            globals()[name] = int(value)

load_note_variables()

# This is the main melody
melody = [
    (C4, 1/4), (D4, 1/4), (E4, 1/4), (F4, 1/4),
    (G4, 1/4), (A4, 1/4), (B4, 1/4), (C5, 1/4),
    (B4, 1/4), (A4, 1/4), (G4, 1), (F4, 1)
]

for pitch, duration in melody:
    clar.play_note(pitch, 0.7, duration)

s.stop_transcribing().to_score().show()

import abjad

def create_score():
    note = abjad.Note("c'4")
    staff = abjad.Staff([note])
    score = abjad.Score([staff])

    return score

def save_score_to_file(score):
    file_path = 'output_score.pdf'
    abjad.persist(score).as_pdf(file_path)
    print(f'Score saved to {file_path}')

if __name__ == "__main__":
    score = create_score()
    save_score_to_file(score)
