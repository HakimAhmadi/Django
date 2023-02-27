from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import Song
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from PIL import Image
from django.http import JsonResponse
from pytube import YouTube
import time
import os
from io import BytesIO
from PIL import Image
import requests
from urllib.request import urlopen

# Create your views here.
def main(request):
  songs=Song.objects.all().values()
  result = {"recent": [],"albums":[],"other":[]}


  for song in songs:
    if default_storage.exists("image/"+song["title"]+".jpg"):
       song["wallpaper"]=True
    else:
       song["wallpaper"]=False    

    if len(result["recent"])< 4:
       result["recent"].append(song)
    result["other"].append(song)

  print(result)

  template = loader.get_template('main.html') 
  return HttpResponse(template.render({'song':result}, request))

def uploadpage(request):
  template = loader.get_template('uploadfile.html')
  return HttpResponse(template.render({}, request))
   
@csrf_protect
def uploadfile(request):
  if request.method == 'POST':
      
      song_title = request.POST['title']
      singer = request.POST['singer']
      # is_album = request.POST.get('isAlbum','')
      # album_title = request.POST.get('album', '')
      release_date = request.POST.get('release_date', '')
      song_type = request.POST['song_type']
      # email = request.POST['email']
      # country = request.POST['country']
      # note = request.POST['note']
    
      image_file = request.FILES.get('image')
      audio_file = request.FILES.get('song')
             
      if audio_file:
      
          default_storage.save('audio/' + f'{song_title}.mp3', audio_file)
                
      if image_file:

          default_storage.save('image/' + f'{song_title}.jpg', image_file)
      
      song = Song(
            title=song_title,
            singer=singer,
            # is_album=is_album,
            # album_title=album_title,
            release_date=release_date,
            song_type=song_type,
            # email=email,
            # country=country,
            # note=note,
        )
        
        # Save the song to the database
      song.save()
      
      return HttpResponse("Form submitted successfully.")
  else:
      return render(request, 'uploadfile.html')

def uploadytpage(request):
   return render(request, 'uploadyt.html')

def loadytfile(request):
    
    if request.method == 'POST':
      video_info = {}
      url = request.POST.get('url')
      # link = "https://www.youtube.com/watch?v=TO-_3tck2tg"
      
      yt = YouTube(url)
      video_info["title"] = yt.title
      video_info["release_date"] = yt.publish_date.date()
      video_info["thumbnail_url"] = yt.thumbnail_url
      video_info["video_url"] = url
      print(video_info)

      return JsonResponse(video_info)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def downloadytfile(request):
   if request.method == 'POST':
      title = request.POST.get('title')
      singer = request.POST.get('singer')
      release_date = request.POST.get('release_date')
      song_type = request.POST.get('song_type')
      video_url = request.POST.get('video_url')

      #saving video as mp3 to media file
      print("------"+video_url)
      yt = YouTube(video_url)
      yt.title = title
      video = yt.streams.filter(abr='128kbps').first()
      destination =  "media/audio/"
      out_file = video.download(output_path=destination)
      base, ext = os.path.splitext(out_file)
      new_file = base + '.mp3'
      os.rename(out_file, new_file)

      # Create image object and saving 
      thumbnail_url = "https://img.youtube.com/vi/"+video_url.split("=")[-1]+"/sddefault.jpg"
      response = urlopen(thumbnail_url)
      image_content = response.read()
      file = BytesIO(image_content)
      default_storage.save("image/"+title+".jpg", file)
      # saving the song data from to database

      song = Song(
            title=title,
            singer=singer,
            release_date=release_date,
            song_type=song_type,
        )
        
      # Save the song to the database
      song.save()

      return render(request, 'main.html')





