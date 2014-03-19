import thread

from time import sleep
from collections import defaultdict

import midievents
import keystroke


handlers = defaultdict(list)


def register(evname, callback):
    handlers[evname].append(callback)


def register_note_to_key(fun):
    def on_note_on(ev):
        note, volume = ev.data1, ev.data2
        if not volume:
            return
    
        key = fun(note)
        
        if key is None:
            return
        if key == 'mouse_click':
            keystroke.click()
        else:
            keystroke.press(key)
    register('NOTE_ON', on_note_on)
    

def handle_event(midi_event):
    event = midievents.midi2event(midi_event)
    for handler in handlers[event.command]:
        handler(event)


def run(inp):
    while True:
        evs = inp.read(256)
        for ev in evs:
            handle_event(ev)
        sleep(0.0001)


def run_threaded(inp):
    thread.start_new_thread(run, (inp,))


def get_inputs(midi):
    infos = [midi.get_device_info(i) for i in range(midi.get_count())]
    return [(pos, info) for pos, info in enumerate(infos) if info[2] == 1]
