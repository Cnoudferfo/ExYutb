import vlc
from ytitem import YTItem
import time

class VLCPlayer:    
    def __init__(self, the_urls):       
        # New a VLC instance
        self.vlc_inst = vlc.Instance("--no-video")
        # New a media list player
        self.media_list_player = self.vlc_inst.media_list_player_new()
        # New a media list
        self.media_list = self.vlc_inst.media_list_new()
        for the_url in the_urls:
            try:
                music_item = YTItem(the_url)
                if music_item is None:
                    print('Panic! No video info found')
                    exit(0)
                print(f'Video Title: {music_item.get_title()}')
                media = self.vlc_inst.media_new(music_item.get_url())
                self.media_list.add_media(media)
                self.media_list_player.set_media_list(self.media_list)
                self.player = self.media_list_player.get_media_player()
            except Exception as e:
                print(f'Error: {e}')
                pass
    def play(self):
        self.media_list_player.play()
    def pause(self):
        self.media_list_player.pause()
    def resume(self):
        self.media_list_player.play()
    def stop(self):
        self.media_list_player.stop()
    def set_volume(self, volume):
        self.player.audio_set_volume(volume)
    def get_volume(self):
        return self.player.audio_get_volume()
    def get_state(self):
        return self.media_list_player.get_state()
    def next(self):
        self.media_list_player.next()
    def previous(self):
        self.media_list_player.previous()

