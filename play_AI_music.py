#
# Set Python version to 3.9.0
#
from asyncio import wait
from scamp import Session

def load_note_variables():
    with open("notes.txt", "r") as file:
        for line in file.readlines():
            name, value = line.strip().split(" ")
            globals()[name] = int(value)

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
                print("Skipping invalid note")
    return melody

def get_pitch_string(pitch):
    with open('notes.txt', 'r') as notes_file:
        lines = notes_file.readlines()
        pitch_mapping = {}
        for line in lines:
            pitch_name, pitch_value = line.strip().split()
            pitch_mapping[int(pitch_value)] = pitch_name
        return pitch_mapping.get(pitch, "Unknown")

if __name__ == "__main__":
    s = Session(tempo=60)
    clar = s.new_part("clarinet", 0)
    load_note_variables()
    melody = load_melody_from_file("melody.txt")
    print(f"melody = {melody}")
    for pitch, duration in melody:
        try:
            pitch_note_name = get_pitch_string(pitch)
            print(f"{pitch_note_name} for {duration} beats")
            volume = 0.7
            if pitch == 0:
                s.wait(duration)
            else:
                clar.play_note(pitch, volume, duration)
        except ValueError as e:
            print("Skipping invalid note:", e)
    print("Melody completed!")