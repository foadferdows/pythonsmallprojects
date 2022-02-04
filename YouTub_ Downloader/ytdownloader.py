

from pytube import YouTube

print("hi! pleas enter the address of video : ")
LINK = input(" >  ")

print("Pleas enter the address of save video : ")
SAVE_PATH = input(" >  ")

try:
    yt = YouTube(LINK)
except:
    print("Connection Error")

try:
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
except:
    print("Some Error!")

print("DONE..!")