from requests_html import HTMLSession
from pytube import YouTube
path = '/home/rahul/Documents/NLP'
session = HTMLSession()
url = "https://www.youtube.com/channel/UCylTmYTHqz482jSFKGwVJ9g/videos"
response = session.get(url)
response.html.render(sleep=1, keep_page = True, scrolldown = 20)

for links in response.html.find('a#video-title'):
    link = next(iter(links.absolute_links))
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)
