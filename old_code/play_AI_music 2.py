# play_AI_music.py
from scamp import Session

s = Session(tempo=120)
clar = s.new_part("clarinet", 0)

def load_note_variables():
    with open("notes.txt", "r") as file:
        for line in file.readlines():
            name, value = line.strip().split(" = ")
            globals()[name] = int(value)

load_note_variables()

def load_melody_from_file(filename):
    melody = []
    with open(filename, "r") as file:
        for line in file.readlines():
            note, duration = line.strip().split(",")
            pitch_string = note.strip()
            duration_value = eval(duration.strip())
            pitch_value = globals().get(pitch_string, pitch_string)
            melody.append((pitch_value, duration_value))
    return melody

melody = load_melody_from_file("melody.txt")

for pitch, duration in melody:
    try:
        print(f"Playing {pitch} for {duration} beats")
        clar.play_note(pitch, 0.7, duration)
    except ValueError as e:
        print("Skipping invalid note:", e)

print("Melody completed!")
