from unittest import TestCase

from src.adapters.mappers.note_translator import translate_note_to_midi_code

class TestMappers(TestCase):
    def test_translate_note_to_midi_code(self):
        note = 0     
        self.assertEqual(note, translate_note_to_midi_code("C-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#-1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B-1"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#0"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B0"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#1"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B1"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#2"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B2"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#3"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B3"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#4"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B4"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#5"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B5"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#6"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B6"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#7"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B7"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G#8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("A#8"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("B8"))
        note += 1

        self.assertEqual(note, translate_note_to_midi_code("C9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("C#9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("D#9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("E9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("F#9"))
        note += 1
        self.assertEqual(note, translate_note_to_midi_code("G9"))

        self.assertEqual(127, note)  