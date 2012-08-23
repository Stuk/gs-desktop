import dbus
from dbus.mainloop.glib import DBusGMainLoop

class MediaKeys(object):

  def __init__(self, cb_obj):
    self.cb_obj = cb_obj

    bus = None
    bus_obj = None

    dbus_loop = DBusGMainLoop()
    bus = dbus.SessionBus(mainloop=dbus_loop)

    bus_obj = bus.get_object('org.gnome.SettingsDaemon',
      '/org/gnome/SettingsDaemon/MediaKeys')
    bus_obj.GrabMediaPlayerKeys(
            'gsdesktop', 0, dbus_interface='org.gnome.SettingsDaemon.MediaKeys')
    bus_obj.connect_to_signal("MediaPlayerKeyPressed", self.keypress)

  def keypress(self, *keys):
    for key in keys:
      if key == "Play":
        self.cb_obj['play_pause']()
      elif key == "Next":
        self.cb_obj['next']()
      elif key == "Previous":
        self.cb_obj['previous']()
