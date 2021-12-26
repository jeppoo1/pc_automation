import urllib.request

### First, get a page source from Chrome inspector, paste the whole text in a .txt file. 
### The text should include a lot of text and also links to the mp4 video files.
# filename = 'C:\\Users\\user\\Desktop\\folder\\videos_text.txt'

### Write everything from the previous text file that includes .mp4 to a list
lista = []
with open(filename, "r", encoding='utf-8') as myFile:
    lines = myFile.readlines()
    for line in lines:
        if ".mp4" in line:
            a = ((str(line)).lstrip()[9:47])
            print(a)
            lista.append(a)

### Use the list to write a new file including only the video links
with open('C:\\Users\\user\\Desktop\\folder\\videos_text.txt', 'w+', encoding='utf-8') as myFile2:
    for i in lista:
        myFile2.write(str(i) + "\n")

### Use urllib.request to download every video file from the links in your list
counter = 0
for url_link in lista:
    if "https" in url_link:
        print(url_link)
        urllib.request.urlretrieve(url_link, "video_" + str(counter) + ".mp4")
        print("------NOW DOWNLOADED: video_" + str(counter) + ".mp4------")
        counter += 1
print("*****COMPLETE******")