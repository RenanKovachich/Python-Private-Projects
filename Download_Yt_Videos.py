#Download vídeos do YouTube
import pytube

url = input("Coloque a URL do Vídeo: ")

print("Coloque onde será salvo (Caso não responder será salvo no destinátario comum)")
destination = str(input(">> ")) or '.'

pytube.YouTube(url).streams.get_highest_resolution().download(destination)
