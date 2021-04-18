#Hello! Just wanted to say Hi!
#My youtube channel!  https://www.youtube.com/channel/UCXu6x7GLqCAVvATkIucIo_Q
#btw after input thats one of my youtube channel videos. replace that with yours!
#Duration is the time of the video
#Range is the ammount of times you want to view the video (make sure it's not too much!)
import webbrowser, time
url = input("https://www.youtube.com/watch?v=zA8E8hFAMGo")
duration = input("16")
for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))
