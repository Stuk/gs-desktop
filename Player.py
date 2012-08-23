import jswebkit
import webkit

class Player(webkit.WebView):
  def __init__(self):
    webkit.WebView.__init__(self)
    self.open("http://listen.grooveshark.com/")
    self.ctx = jswebkit.JSContext(self.get_main_frame().get_global_context())

  def play_pause(self):
    self.execute_script("document.getElementById('player_play_pause').click()")
    print self.get_song()

  def next(self):
    self.execute_script("document.getElementById('player_next').click()")

  def previous(self):
    self.execute_script("document.getElementById('player_previous').click()")

  def get_song(self):
    if self.ctx.EvaluateScript("document.getElementById('playerDetails_nowPlaying').childElementCount"):
      song = self.ctx.EvaluateScript("document.getElementById('playerDetails_nowPlaying').getElementsByClassName('song')[0].textContent");
      artist = self.ctx.EvaluateScript("document.getElementById('playerDetails_nowPlaying').getElementsByClassName('artist')[0].textContent");
      album = self.ctx.EvaluateScript("document.getElementById('playerDetails_nowPlaying').getElementsByClassName('album')[0].textContent");
      return {"song": song, "artist": artist, "album": album}
    else:
      return 'Not playing.'
