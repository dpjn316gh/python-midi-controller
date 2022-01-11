NOTES = {'C': 0,
         'D': 2,
         'E': 4,
         'F': 5,
         'G': 7,
         'A': 9,
         'B': 11,
         }


def translate_note_to_midi_code(note: str) -> int:

    def get_octave(number: str) -> int:
        try:
            octave = int(number)
        except:
            raise ValueError(f"{number} must be numeric. Values are integers between -1 to 9")
        if not -1 <= octave <= 9:
            raise ValueError(f"{number} Values must be integers between -1 to 9")
        return int(number)

    if not 2 <= len(note) <= 4:
        raise ValueError(f"{note} must be between C-1 and G9")
    if note[0].upper() not in "ABCDEFG":
        raise ValueError(f"{note} must be one of the following A, B, C, D, E, F, or G")
    midi_note = NOTES[note[0].upper()]
    if note[1] == "#": 
        midi_note += 1
        midi_note_octave = get_octave(note[2:])
    else:
        midi_note_octave = get_octave(note[1:])

    midi_note = midi_note + (midi_note_octave + 1) * 12
    if not 0 <= midi_note <= 127:
        raise ValueError(f"{midi_note} if out of range")
    return midi_note