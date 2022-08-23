#Prog para abrir url
import webbrowser
while True:
    url = input("Coloque a url: ")
    webbrowser.open(url)
    
    webbrowser.open_new(url)
    
    webbrowser.open_new_tab(url)