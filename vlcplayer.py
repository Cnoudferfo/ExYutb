import vlc
from ytitems import YTItems

class VLCPlayer:    
    def __init__(self, the_urls):
        # Call YTItems to get the YT items' information including real URLs
        yt_items = YTItems(the_urls).get_items()
        # New a VLC instance
        self.vlc_inst = vlc.Instance("--no-video")
        # New a media list player
        self.media_list_player = self.vlc_inst.media_list_player_new()
        # New a media list
        self.media_list = self.vlc_inst.media_list_new()
        # Create new media according to the real URLs and add them to the media list   
        self.info_list= []     
        for item in yt_items:
            media = self.vlc_inst.media_new(item['url'])
            self.media_list.add_media(media)
            self.info_list.append({"title": item['title'], "duration": item['duration']})
        # To set the media list to the media list player
        self.media_list_player.set_media_list(self.media_list)
        # To get the player from the media list player
        self.player = self.media_list_player.get_media_player()
    
    def release(self):
        #stop the media list player
        self.media_list_player.stop()
        #release the media list player
        self.media_list_player.release()
        #release the media list
        self.media_list.release()
        #release the VLC instance
        self.vlc_inst.release()

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
    def is_stopped(self):
        st = self.media_list_player.get_state()
        if st == vlc.State.Ended or st == vlc.State.Error or st == vlc.State.Stopped:
            return True
    def next(self):
        self.media_list_player.next()
    def previous(self):
        self.media_list_player.previous()

