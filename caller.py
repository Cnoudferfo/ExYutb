import ytplaylists
import platform
import os
import time

# To detect if in SSH or not
if platform.system() == 'Linux' and os.environ.get('SSH_CONNECTION') is not None:
    print('In SSH mode')
    from kbsshkb import KbApp
else:
    print('Not in SSH mode')
    from kbpynput import KbApp
from vlcplayer import VLCPlayer

CALLER_STATES = ('IDLE', 'PLAYING', 'PAUSED', 'STOPPED')

the_vlc_player = None

def a_sample_kb_handler(key) -> bool:
    global the_vlc_player
    if key == 'g':
        print('Play...')
        the_vlc_player.play()
        return True
    elif key == 'p':
        print('Pause...')
        the_vlc_player.pause()
        return True
    elif key == 'r':
        print('Resume...')
        the_vlc_player.play()
        return True
    elif key == 's':
        print('Stop...')
        the_vlc_player.stop()
        return True
    elif key == 'l':
        print('Next...')
        the_vlc_player.next()
        return True
    elif key == 'h':
        print('Previous...')
        the_vlc_player.previous()
        return True
    elif key == 'u':
        print('Volume up...')
        the_v = the_vlc_player.get_volume()
        the_v += 10
        the_vlc_player.set_volume(the_v)
        return True
    elif key == 'd':
        print('Volume down...')
        the_v = the_vlc_player.get_volume()
        the_v -= 10
        the_vlc_player.set_volume(the_v)
        return True
    elif key == 'q':
        # Release the player
        print('Release the player...')
        the_vlc_player.release()
        print('Quit...')
        return False
    else:
        print(f'a_kb_handler: {key} pressed')
        return True
def list_usage():
    print('Usage:[q] quit, [g] play, [p] pause, [r] resume, [s] stop, [u] vloume up, [d] volume down, [l] next, [h] previous')
def list_states():
    print(f'States: {CALLER_STATES}')
if __name__ == '__main__':
    # ypls : YTPlayLists
    ypls = ytplaylists.YTPlayLists()
    # the_chosen_playlist = ypls.search_playlist_by_title('Joyful')[0]
    the_chosen_playlist = ypls.list_my_playlists_and_pick_one()
    the_playlist_items = ypls.get_playlist_items(the_chosen_playlist['id'])
    for item in the_playlist_items:
        print(f'Title: {item["title"]}, Video ID: {item["video_id"]}')
    the_urls_4 = [f'https://music.youtube.com/watch?v={item["video_id"]}' for item in the_playlist_items]
    the_vlc_player = VLCPlayer(the_urls_4)
    the_vlc_player.set_volume(40)

    list_usage()
    app = KbApp(a_sample_kb_handler)
