
#importing the module 
from pytube import YouTube 
  
#where to save 
SAVE_PATH = "D:/" #to_do 
  
#link of the video to be downloaded
l = [
    'https://www.youtube.com/watch?v=9d3X8eBov1M&list=PLhs1urmduZ29jTcE1ca8Z6bZNvH_39ayL&index=1',
    'https://www.youtube.com/watch?v=SsV29noHQRU&list=PLhs1urmduZ29jTcE1ca8Z6bZNvH_39ayL&index=2',
]
'''
#taking input link
while True:
    s = input()
    try:
        s = int(s)
        if s==-1:
        break
    except:
        pass
    l.append(s)
'''
for link in l:
  
    try: 
        #object creation using YouTube which was imported in the beginning 
        yt = YouTube(link) 
    except: 
        print("Could not download!") #to handle exception 
      
    #filters out all the files with "mp4" extension
    v = yt.streams.first()
    v.download(SAVE_PATH)
    print('completed',link)
