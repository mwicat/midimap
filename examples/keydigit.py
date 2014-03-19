from pygame import midi

import midimap.midihandlers as midihandlers


# http://www.midimountain.com/midi/midi_note_numbers.html
WHITE_KEYS = [0, 2, 4, 5, 7, 9, 11, 12]


def note_to_key(note):
    note %= 12  # Drop note octave, leave pitch class
    if note in WHITE_KEYS:
        # Map note C to '1', D to '2' and so on...
        white_num = WHITE_KEYS.index(note) + 1
        return str(white_num)
    else:
        # Every black note triggers mouse click
        return 'mouse_click'


def main():
    # Initialize Pygame midi subsystem
    midi.init()
    
    # Register our handler which translates midi notes to keybaord keys
    midihandlers.register_note_to_key(note_to_key)
    
    # Listen on every MIDI input found on system
    for pos, info in midihandlers.get_inputs(midi):
        try:
            (interf, name, input, output, opened) = info
            print 'Listening on', name
            # Run event listener for this input in its own thread
            midihandlers.run_threaded(midi.Input(pos))
        except Exception as e:
            print e

    raw_input('Press enter to exit')
    

if __name__ == '__main__':
    main()
