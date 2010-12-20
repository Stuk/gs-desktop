#!/usr/bin/env python

import gtk

from Player import Player
from MediaKeys import MediaKeys

player = Player()

mediakeys = MediaKeys({
  "play_pause": player.play_pause,
  "next": player.next,
  "previous": player.previous
})

sw = gtk.ScrolledWindow()
sw.add(player)

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
win.set_title("Grooveshark")
win.set_default_size(800, 600)
win.connect("destroy", gtk.main_quit)

win.add(sw)
win.show_all()

gtk.main()
