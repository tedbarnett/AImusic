from scamp import Session

# Create a session
session = Session()

# Define the melody
melody = [60, 62, 64, 65, 67, 69, 71, 72]

# Define note lengths (in quarter notes)
note_lengths = [1, 1, 1, 1, 1, 1, 1, 1]

# Define the volume (0 to 1)
volume = 0.8

# Play the melody
violin = session.new_part("violin")
for pitch, length in zip(melody, note_lengths):
    violin.play_note(pitch, length, volume)

# Wait for the music to finish
session.wait_for_children_to_finish()
