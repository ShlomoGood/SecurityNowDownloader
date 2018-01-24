# Shlomo Goodman
#Python script for downloading episodes of the Security Now podcast
#Can download high or low quality audio
#Prints after successful download of each episode.
#Tracks and prints amount of time to download all episodes
#Prints amount of time to download past "five" episodes

#provides web access
import urllib.request
#track time it takes to download
import timeit

import os

#takes in a url, the quality requested, and folder path/name
#downloads the audio into specified file
def download_pdf(url,quality,folder):
    if(num < 100):
       if(quality == "h"):
           name = "sn000" + str(num)
       elif(quality == "l"):
           name = "sn-00" + str(num)
    elif (num < 100):
        if(quality == "h"):
            name = "sn00" + str(num)
        elif(quality == "l"):
            name = "sn-0" + str(num)
    elif (num < 1000):
        if(quality == "h"):
            name = "sn0" + str(num)
        elif(quality == "l"):
            name = "sn-" + str(num)
    if(quality == "h"):
        nameMp3 = name+".mp3"
    elif(quality == "l"):
        nameMp3 = name+"-lq.mp3"
    if(quality == "h"):
        fullName = os.path.join(folder,nameMp3)
    elif(quality == "l"):
        fullName = os.path.join(folder,nameMp3)
    #print(url)
    urllib.request.urlretrieve(url,fullName)

def time_convert(time):
    time = time / 1
    print(time)
    hour = 360
    minute = 60
    hourCounter = 0
    minCounter = 0
    totalTime = ""
    while(time > 0):
        print(time)
        
   
#Main
end = 647 #Latest episode
action = input("Which quality do you want? (h = high quality,l = low quality): ")
begin = input("Which episode do you want to start from: ")
begin = int(begin)
num = begin
beginTime = timeit.default_timer()
start = beginTime

while (num <= end):
    #set download location, folder is the download location
    if(action == "h"):
        folder = 'C:/Users/Shlomo/Desktop/SecurityNow/SN-highQuality'
    elif(action == "l"):
        folder = 'C:/Users/Shlomo/Desktop/SecurityNow/SN-lowQuality'

    #There are two episodes that I was unable to download or find specific links for
    #feel free to add specific links or inform me of them 
    if ((num == 436) | (num == 540)):
        print("Episode " + str(num) + " wasn't found")
    elif((num == 592) & (action == "l")):
         print("Episode 592 wasn't found")
    else:
        if(num < 10):
            if(action == "h"):
                website = "http://twit.cachefly.net/audio/sn/sn000" + str(num) + "/sn000" + str(num) + ".mp3"
            elif(action == "l"):
                website = "http://media.grc.com/SN/sn-00" + str(num) + "-lq.mp3"
        elif (num < 100):
            if (action == "h"):
                website = "http://twit.cachefly.net/audio/sn/sn00" + str(num) + "/sn00" + str(num) + ".mp3"
            elif(action == "l"):
                website = "http://media.grc.com/SN/sn-0" + str(num) + "-lq.mp3"
        elif (num >= 100):
            if(action == "h"):
                website = "http://twit.cachefly.net/audio/sn/sn0" + str(num) + "/sn0" + str(num) + ".mp3"
            elif(action == "l"):
                website = "http://media.grc.com/SN/sn-" + str(num) + "-lq.mp3"
        download_pdf(website,action,folder)
        print("Episode " + str(num) + " downloaded successfully.")

    #timer isn't based on actual downloads, it's based on the starting episode number entered by the user
    if((num % 5) == 0):
        stop = timeit.default_timer()
        total = (((stop - start) / 1) - ((stop - start) % 1))
        print("It took " + str(total) + " seconds to download the last 5 episodes")
        start = stop
    num +=1
    

    
print("All Security Now episodes (from " + str(begin) + " to " + str(end) + ") downloaded successfully.")
print("It took " + str(stop - beginTime) +   " seconds to download these " + str((end - begin) + 1) + " episodes")                
