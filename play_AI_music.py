# play_AI_music.py
from asyncio import wait
from scamp import Session

s = Session(tempo=60)
clar = s.new_part("violin", 0)

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
            try:
                note, duration = line.strip().split(",")
                if "/" in duration:
                    numerator, denominator = map(int, duration.split("/"))
                    duration = numerator / denominator
                    duration = float(duration)
                pitch_string = note.strip()
                duration_value = eval(duration.strip())
                pitch_value = globals().get(pitch_string, pitch_string)
                melody.append((pitch_value, duration_value))
            except ValueError:
                print(f"{line.strip()}")
    return melody



def get_pitch_string(pitch_value):
    pitch_map = {value: key for key, value in globals().items() if isinstance(value, float)}
    return pitch_map.get(pitch_value, f"Unknown pitch value {pitch_value}")


for pitch, duration in melody:
    try:
        pitch_note_name = get_pitch_string(str(pitch))
        print(f"Playing {pitch_note_name} for {duration} beats")
        volume = 0.7
        if pitch == 0:
            wait(duration)
            print("Resting")
        else:
            clar.play_note(pitch, volume, duration)
    except ValueError as e:
        print("Skipping invalid note:", e)

print("Melody completed!")
melody = load_melody_from_file("melody.txt")
print(f"melody = {melody}")
