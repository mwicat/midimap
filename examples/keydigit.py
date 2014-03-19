from pygame import midi

import midimap.midihandlers as midihandlers


WHITE_KEYS = [0, 2, 4, 5, 7, 9, 11, 12]


def note_to_key(note):
    note %= 12
    if note in WHITE_KEYS:
        white_num = WHITE_KEYS.index(note) + 1
        return str(white_num)
    else:
        return 'mouse_click'


def main():
    midi.init()
    
    midihandlers.register_note_to_key(note_to_key)
    
    for pos, info in midihandlers.get_inputs(midi):
        try:
            (interf, name, input, output, opened) = info
            print 'Listening on', name
            midihandlers.run_threaded(midi.Input(pos))
        except Exception as e:
            print e
        
    raw_input('Press enter to exit')
    

if __name__ == '__main__':
    main()
