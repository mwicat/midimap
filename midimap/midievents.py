# Stolen from
# https://www.pygame.org/docs/ref/midi.html#comment_pygame_midi_midis2events

# A slightly more readable midis2events. More parsing can be done, but I didn't
# need to...

import pygame.event
import pygame.midi


# Incomplete listing:
COMMANDS = {0: "NOTE_OFF",
            1: "NOTE_ON",
            2: "KEY_AFTER_TOUCH",
            3: "CONTROLLER_CHANGE",
            4: "PROGRAM_CHANGE",
            5: "CHANNEL_AFTER_TOUCH",
            6: "PITCH_BEND"}


# Incomplete listing: this is the key to CONTROLLER_CHANGE events data1
CONTROLLER_CHANGES = {1: "MOD WHEEL",
                      2: "BREATH",
                      4: "FOOT",
                      5: "PORTAMENTO",
                      6: "DATA",
                      7: "VOLUME",
                      10: "PAN",
                      }


def midi2event(midi, device_id=None):
    ((status,data1,data2,data3),timestamp) = midi
    if status == 0xFF:
        # pygame doesn't seem to get these, so I didn't decode
        command = "META"
        channel = None
    else:
        try:
            command = COMMANDS[ (status & 0x70) >> 4]
        except:
            command = status & 0x70
        channel = status & 0x0F
    e = pygame.event.Event(pygame.midi.MIDIIN,
                           status=status,
                           command=command,
                           channel=channel,
                           data1=data1,
                           data2=data2,
                           timestamp=timestamp,
                           device_id=device_id)
    return e