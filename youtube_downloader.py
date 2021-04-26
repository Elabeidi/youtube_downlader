from pytube import YouTube

link = input('Enter the link : ')

video = YouTube(link)

#print(f"Video title is : \n-----------------------")
#print(f"Video description is :\n {video.description} \n----------------------------------")
#print(f"Video views are :{video.views} \n--------------------------------")
#print(f"Video rate is :{video.rating}\n--------------------------------")
#print(f"Video during is {video.length} seconds\n--------------------------------")

# print(video.streams)

#for stream in video.streams:
   # print(stream)
   
#for stream in video.streams.filter(progressive=True):
   # print(stream)
#for stream in video.streams.filter(subtype= "mp4"):
   # print(stream)
 
#for stream in video.streams.filter(res=10):
    #print(stream)   
    
def finish():
    print("download done")
    
#print(video.streams.get_highest_resolution())
print(video.streams.get_lowest_resolution())

video.streams.get_lowest_resolution().download(output_path="")# add the storage folder
video.register_on_complete_callback(finish())