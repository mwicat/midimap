=============
Midimap
=============

This library allows you to translate MIDI events coming from devices to
operating system keystrokes. For example, you can translate C1 note
from MIDI keyboard to simulate letter 'C' typed with PC keyboard.

At the moment, it only works on Windows but can be easily ported to
*NIX if proper `midimap/keystroke.py` analogue is given.

A simple example is attached in `examples/keydigit.py` directory.

Dependencies
------------

* _Pygame: http://www.pygame.org/download.shtml

Installation
------------

From source
~~~~~~~~~~~~~

To install using `pip`::

	pip install -e git+https://github.com/mwicat/midimap.git#egg=midimap

Ensure you have Pygame installed on your system, for Debian::

	sudo apt-get install python-pygame

