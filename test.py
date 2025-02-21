# importing vlc module 
import vlc 
  
# importing time module 
import time 
  
# creating a media player object 
media_player = vlc.MediaListPlayer() 
  
# creating Instance class object 
player = vlc.Instance() 
  
# creating a new media list 
media_list = player.media_list_new() 
  
# creating a new media 
media = player.media_new("test1.mp3") 
  
# adding media to media list 
media_list.add_media(media)

media = player.media_new("test2.mp3")
media_list.add_media(media)
  
# setting media list to the media player 
media_player.set_media_list(media_list) 
  
# new media player instance 
new = player.media_player_new()
new.audio_set_volume(50) 
# setting media player to it 
media_player.set_media_player(new) 
  
# start playing video 
media_player.play() 
  
# wait so the video can be played for 5 seconds 
# irrespective for length of video 
time.sleep(5)

current_volume = new.audio_get_volume()

print(f'volume: {current_volume}')
  
# getting media player instance 
value = media_player.get_media_player() 
  
# printing value 
print(value) 

try:
    mul = -1
    cnt = 0
    while True:
        state = media_player.get_state()
        print(f'media_player State: {state}')
        if state in [vlc.State.Ended, vlc.State.Error]:
            break
        time.sleep(5)
        current_volume = current_volume + mul * 20  * -1
        mul = mul * -1
        new.audio_set_volume(current_volume)
        print(f'volume: {current_volume}')
        cnt = cnt + 1
        if cnt > 5:
            cnt = 0
            print('next...')
            media_player.next()
except KeyboardInterrupt:
    print('Ctrl+C detected!')
    media_player.stop()