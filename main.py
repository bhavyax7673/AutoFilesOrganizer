from os import listdir,path
from shutil import move
from time import sleep

target_location = "C://Users//DELL//Downloads//"

store_images_location = "C://Users//DELL//Pictures//"
store_videos_location = "C://Users//DELL//Videos//"
store_docs_location = "C://Users//DELL//Documents//"
store_audio_location = "C://Users//DELL//Audio//"

images = ["png","jpg","jpeg"]
audio = ["mp3"]
video = ["mp4","mkv"]
documents = ["pdf","docx","txt","json","ppt","pptx","doc"]

while True:
    all_files_present = listdir(target_location)
        
    for i in all_files_present:
    
        if "." in i:

            extension = i.split(".")
            extension = extension[len(extension)-1]
            
            if extension in images:
                print(f"{i} Moved to {store_images_location}\n")
                move(
                    path.join(target_location,i),
                    path.join(store_images_location))
                
            elif extension in documents:
                print(f"{i} Moved to {store_docs_location}\n")
                move(
                    path.join(target_location,i),
                    path.join(store_docs_location))
                
            elif extension in audio:
                print(f"{i} Moved to {store_audio_location}\n")
                move(
                    path.join(target_location,i),
                    path.join(store_audio_location))
                
            elif extension in documents:
                print(f"{i} Moved to {store_videos_location}\n")
                move(
                    path.join(target_location,i),
                    path.join(store_videos_location))

            else:
                continue

    sleep(60*60)