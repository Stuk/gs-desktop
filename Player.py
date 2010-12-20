import webkit

class Player(webkit.WebView):
  def __init__(self):
    webkit.WebView.__init__(self)
    self.open("http://listen.grooveshark.com/")
    #self.connect("title-changed", self._title_changed_cb)

  def play_pause(self):
    self.execute_script("document.getElementById('player_play_pause').click()")
    print self.get_song()

  def next(self):
    self.execute_script("document.getElementById('player_next').click()")

  def previous(self):
    self.execute_script("document.getElementById('player_previous').click()")

  def get_song(self):
    # What a hack. The only way to pass info back to python is through the
    # title of the page!
    self.execute_script("""
      np=document.getElementById('playerDetails_nowPlaying')
      song=np.getElementsByClassName('song')[1].textContent
      artist=np.getElementsByClassName('artist')[0].textContent
      album=np.getElementsByClassName('album')[0].textContent
      document.title = song+'||'+artist+'||'+album
    """)

    parts = self.get_main_frame().get_title().split('||')

    return {"song": parts[0], "artist": parts[1], "album": parts[2]}
