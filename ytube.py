from pytube import YouTube

def audiol(yt):
    logs = yt.streams.filter(only_audio=True).all
    print(logs)

def videol(yt):
    logs = yt.streams.filter(only_video=True).all
    print(logs)

def allc(yt):
    logs = yt.streams.all
    print(logs)

link = input("Enter the video link:")

try:
    yt = YouTube(link)
except:
    print("Video not found")

print("filter file")
filetype = input("video/audio/all:")

if filetype == "video":
    videol(yt)
elif filetype == "audio":
    audiol(yt)
elif filetype == "all":
    allc(yt)
else:
    print("invalid input")

ival = int(input("Enter the itag value:"))
yt.streams.get_by_itag(ival).download()