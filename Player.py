import gtk
import jswebkit
import webkit

class Player(webkit.WebView):
  def __init__(self):
    webkit.WebView.__init__(self)
    self.open("http://listen.grooveshark.com/")
    self.ctx = jswebkit.JSContext(self.get_main_frame().get_global_context())
    gtk.timeout_add(1000, self.get_song)

  def play_pause(self):
    self.execute_script("document.getElementById('player_play_pause').click()")

  def next(self):
    self.execute_script("document.getElementById('player_next').click()")

  def previous(self):
    self.execute_script("document.getElementById('player_previous').click()")

  def get_song(self):
    if self.ctx.EvaluateScript("var p = document.getElementById('playerDetails_nowPlaying');p && p.childElementCount"):
      if self.ctx.EvaluateScript("document.querySelector('.player_control.play')"):
        self.get_parent_window().set_title('Grooveshark - Paused')
      else:
        song = self.ctx.EvaluateScript("document.querySelector('#playerDetails_nowPlaying .song').textContent");
        artist = self.ctx.EvaluateScript("document.querySelector('#playerDetails_nowPlaying .artist').textContent");
        album = self.ctx.EvaluateScript("document.querySelector('#playerDetails_nowPlaying .album').textContent");

        self.get_parent_window().set_title('Grooveshark - Playing: %s by %s on %s' % (song, artist, album))
    else:
      self.get_parent_window().set_title('Grooveshark - Not Playing')
    
    gtk.timeout_add(1000, self.get_song)
