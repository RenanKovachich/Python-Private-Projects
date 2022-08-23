#Download Youtube vídeo para mp3
from unicodedata import decomposition
from pytube import YouTube
import os

yt = YouTube(str(input("Coloque a URL do vídeo que você quer baixar: \n>> ")))

video = yt.streams.filter(only_audio=True).first()

print("Coloque onde será salvo (Caso não responder será salvo no destinátario comum)")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + "foi feito a conversão corretamente.")