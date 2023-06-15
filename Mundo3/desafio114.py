import urllib.request

try:
    site = urllib.request.urlopen("https://www.twitch.tv/coreano")
except:
    print("Deu erro")
else:
    print("Deu certo")
    print(site.read())