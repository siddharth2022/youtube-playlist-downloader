import logging
from pytube import Playlist
from pytube import request
from pytube.__main__ import YouTube

logger = logging.getLogger(__name__)


##-------------------------Write your playlist Url below------------
url="https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"




class Playlist(object):

    def __init__(self, url):
        self.playlist_url = url
        self.video_urls = []

    def construct_playlist_url(self):

        if 'watch?v=' in self.playlist_url:
            base_url = 'https://www.youtube.com/playlist?list='
            playlist_code = self.playlist_url.split('&list=')[1]
            return base_url + playlist_code

        # url is already in the desired format, so just return it
        return self.playlist_url

    def parse_links(self):
        url = self.construct_playlist_url()
        req = request.get(url)

        # split the page source by line and process each line
        content = [x for x in req.split('\n') if 'pl-video-title-link' in x]
        link_list = [x.split('href="', 1)[1].split('&', 1)[0] for x in content]

        return link_list

    def populate_video_urls(self):
        base_url = 'https://www.youtube.com'
        link_list = self.parse_links()

        for video_id in link_list:
            complete_url = base_url + video_id
            self.video_urls.append(complete_url)

    def download_all(self, download_path=None):

        self.populate_video_urls()
        logger.debug('total videos found: ', len(self.video_urls))
        logger.debug('starting download')

        for link in self.video_urls:
            yt = YouTube(link)
            
            dl_stream = yt.streams.filter(
                progressive=True, subtype='mp4',
            ).order_by('resolution').desc().first()

            logger.debug('download path: %s', download_path)
            dl_stream.download(download_path)
            logger.debug('download complete')
            tube = YouTube(url)
            title = tube.title
            caption = tube.captions.get_by_language_code('en')
            if caption is not None:
                subtitle = caption.generate_srt_captions()
                file = open(title+".srt", "w")
                if file.writelines(subtitle) :
                 print "subtitle file has saved"





pl = Playlist(url)
pl.populate_video_urls()
no = len(pl.video_urls)
print "there is total %s:" % len(pl.video_urls) 
print " videos available in playlist"

print "This are available files in your current directory"
print "Enter the number of videos downloaded of playlist"
num=input()
for i in range(num,no-1):
    print "downloading "+str(i+1)+" video started"
    url = pl.video_urls[i]
    YouTube(url).streams.first().download()
    print "video "+str(i+1)+" download complete"
    tube = YouTube(url)
    title = tube.title
    caption = tube.captions.get_by_language_code('en')
    if caption is not None:
                print "downloadind subtitle for "+str(i+1)+" video"
                subtitle = caption.generate_srt_captions()
                file = open(title+".srt", "w")
                file.writelines(subtitle) 
                print "subtitle file has saved"
            
            

#pl.download_all()
#yt = YouTube("https://www.youtube.com/watch?v=eVTXPUF4Oz4&list=PL93lkIr4wEXFyrkvOaxzmgBPkOiOKMX4t&t=0s&index=2")
#yt.streams.all()
