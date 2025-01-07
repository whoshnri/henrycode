import pytube as pt

url = 'https://www.youtube.com/watch?v=jTJvyKZDFsY'
vid = pt.YouTube(url)

try:
    vid00 = vid.streams.get_by_itag(18)
    vid00.download('vid.mp4')

except Exception as e:
    print(e)



