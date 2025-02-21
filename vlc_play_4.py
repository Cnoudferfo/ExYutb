# Description: This script plays a list of YouTube videos using VLC Python bindings.
# Install the required libraries:
# > pip install python-vlc
# > pip install yt-dlp
#
import ytplaylists
import vlc
from ytitem import YTItem
import time

if __name__ == '__main__':
    the_yt_playlist = ytplaylists.YTPlayLists()
    the_chosen_playlist = the_yt_playlist.get_playlist_id('Newfav')[0]
    the_playlist_items = the_yt_playlist.get_playlist_items(the_chosen_playlist['id'])
    for item in the_playlist_items:
        print(f'Title: {item["title"]}, Video ID: {item["video_id"]}')
    the_urls_4 = [f'https://music.youtube.com/watch?v={item["video_id"]}' for item in the_playlist_items]
    
    print(f'VLC Version: {vlc.libvlc_get_version()}')
    # New a VLC instance
    vlc_inst = vlc.Instance("--no-video")
    # New a media list player
    media_list_palyer = vlc_inst.media_list_player_new()
    # New a media list
    media_list = vlc_inst.media_list_new()
       
    for the_url in the_urls_4:
        music_item = YTItem(the_url)
        if music_item is None:
            print('Panic! No video info found')
            exit(0)
        print(f'Video Title: {music_item.get_title()}')
        media = vlc_inst.media_new(music_item.get_url())
        media_list.add_media(media)
    
    media_list_palyer.set_media_list(media_list)
    player = media_list_palyer.get_media_player()
    
    # To set the volume to 50%
    player.audio_set_volume(50)
    print(f'Audio volume: {player.audio_get_volume()}')
    media_list_palyer.play()

    try:
        while True:
            state = media_list_palyer.get_state()
            # print(f'Player State: {state}')
            if state in [vlc.State.Ended, vlc.State.Error]:
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print('Ctrl+C detected!')
        media_list_palyer.stop()
        exit(0)
    